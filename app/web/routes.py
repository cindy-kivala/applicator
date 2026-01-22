"""
Web interface routes
"""

from flask import render_template, redirect, url_for, flash, request
from app.web import web_bp
from app.database import db

@web_bp.route('/')
def index():
    """Landing page"""
    # Pass some sample data to template
    stats = {
        'new_jobs_today': 0,
        'applications_sent': 0,
        'high_priority': 0,
        'interviews': 0
    }
    return render_template('index.html', 
                         stats=stats,
                         high_priority_jobs=[],
                         recent_activities=[],
                         last_sync='Never')

@web_bp.route('/dashboard')
def dashboard():
    """Dashboard page"""
    metrics = {
        'total_jobs': 0,
        'new_today': 0,
        'applications': 0,
        'response_rate': 0,
        'interviews': 0,
        'upcoming': 0,
        'offers': 0,
        'pending_offers': 0
    }
    
    pipeline = {
        'interested': 0,
        'applied': 0,
        'interview': 0,
        'offer': 0
    }
    
    return render_template('dashboard.html',
                         metrics=metrics,
                         pipeline=pipeline,
                         recent_applications=[],
                         top_matches=[],
                         upcoming_tasks=[],
                         upcoming_interviews=[],
                         coding={},
                         weekly={})

@web_bp.route('/jobs')
def jobs():
    """Browse jobs page"""
    return render_template('jobs.html', jobs=[])

@web_bp.route('/applications')
def applications():
    """Applications tracking page"""
    stats = {
        'interested': 0,
        'applied': 0,
        'interview': 0,
        'offer': 0,
        'rejected': 0
    }
    return render_template('applications.html',
                         stats=stats,
                         interested=[],
                         applied=[],
                         interview=[],
                         offer=[],
                         rejected=[],
                         all_applications=[])

@web_bp.route('/profile')
def profile():
    """User profile page"""
    profile_data = {
        'name': 'Cindy Kivala',
        'email': 'cindykivala@gmail.com',
        'phone': '',
        'location': 'Nairobi, Kenya',
        'linkedin': '',
        'github': '',
        'portfolio': ''
    }
    return render_template('profile.html',
                         profile=profile_data,
                         experience=[],
                         education=[],
                         skills={},
                         preferences={},
                         documents=[])

@web_bp.route('/analytics')
def analytics():
    """Analytics page"""
    metrics = {
        'total_applications': 0,
        'response_rate': 0,
        'interviews': 0,
        'avg_response_time': 0
    }
    return render_template('analytics.html',
                         metrics=metrics,
                         source_performance=[],
                         skills_gap=[])

@web_bp.route('/coding-platforms')
def coding_platforms():
    """Coding platforms tracking page"""
    return render_template('coding_platforms.html',
                         platforms={},
                         recommendations=[],
                         assessments=[])