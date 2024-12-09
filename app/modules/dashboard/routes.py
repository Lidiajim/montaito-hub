from flask import render_template
from app.modules.dashboard import dashboard_bp
from app.modules.dashboard.services import DashboardService
from app.modules.profile.services import UserProfileService
from flask_login import login_required, current_user


dashboard_service = DashboardService()
profile_service = UserProfileService()

@dashboard_bp.route('/dashboard', methods=['GET'])
def index():
    dashboard_data = dashboard_service.get_dashboard_public_data()

    return render_template('dashboard/index.html', data=dashboard_data)


@dashboard_bp.route("/dashboard/profile", methods=['GET'])
@login_required
def index_id():    
    dashboard_data = dashboard_service.get_dashboard_user_data(current_user.id)

    return render_template('dashboard/profile_dashboard.html', data=dashboard_data)