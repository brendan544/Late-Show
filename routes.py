from flask import Flask, jsonify, request
from models import db, Episode, Guest, Appearance

def create_routes(app):
    @app.route('/episodes', methods=['GET'])
    def get_episodes():
        episodes = Episode.query.all()
        return jsonify([episode.to_dict() for episode in episodes])

    @app.route('/episodes/<int:id>', methods=['GET'])
    def get_episode(id):
        episode = Episode.query.get(id)
        if not episode:
            return jsonify({"error": "Episode not found"}), 404
        
        appearances = []
        for appearance in episode.appearances:
            appearances.append({
                "episode_id": appearance.episode_id,
                "guest": appearance.guest.to_dict(),
                "guest_id": appearance.guest_id,
                "id": appearance.id,
                "rating": appearance.rating
            })

        episode_data = episode.to_dict()
        episode_data['appearances'] = appearances
        return jsonify(episode_data), 200

    @app.route('/guests', methods=['GET'])
    def get_guests():
        guests = Guest.query.all()
        return jsonify([guest.to_dict() for guest in guests])

    @app.route('/appearances', methods=['POST'])
    def create_appearance():
        data = request.get_json()
        new_appearance = Appearance(
            rating=data['rating'],
            episode_id=data['episode_id'],
            guest_id=data['guest_id']
        )
        db.session.add(new_appearance)
        try:
            db.session.commit()
            return jsonify(new_appearance.to_dict()), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"errors": ["validation errors"]}), 400

    @app.route('/episodes/<int:id>', methods=['DELETE'])
    def delete_episode(id):
        episode = Episode.query.get(id)
        if not episode:
            return jsonify({"error": "Episode not found"}), 404
        
        db.session.delete(episode)
        db.session.commit()
        return jsonify({"message": "Episode deleted successfully"}), 200