#!/usr/bin/env bash
# ============================================================
# TROVIA – Automated Local Setup Script
# Run: bash setup.sh
# ============================================================
set -e

echo ""
echo "🚀  Setting up TROVIA..."
echo ""

# 1. Create virtual environment
if [ ! -d "venv" ]; then
    echo "📦  Creating virtual environment..."
    python3 -m venv venv
fi

# 2. Activate
source venv/bin/activate
echo "✅  Virtual environment activated"

# 3. Upgrade pip
pip install --upgrade pip --quiet

# 4. Install dependencies
echo "📥  Installing dependencies..."
pip install -r requirements/base.txt
echo "✅  Base dependencies installed"

# 5. Install dev extras (optional, won't fail if debug-toolbar unavailable)
pip install django-debug-toolbar==4.3.0 || echo "⚠️  debug-toolbar skipped"

# 6. Copy .env if not exists
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "⚙️   Created .env from .env.example"
    echo "    → Edit .env to set your own SECRET_KEY before going to production!"
fi

# 7. Run migrations
echo "🗃️   Running migrations..."
python manage.py migrate --settings=trovia.settings.dev

# 8. Create superusers
echo "👤  Creating superusers (Troey & Silvia)..."
python manage.py create_superusers --settings=trovia.settings.dev || echo "   (superusers may already exist)"

# 9. Collect static files
echo "📁  Collecting static files..."
python manage.py collectstatic --settings=trovia.settings.dev --noinput --quiet

echo ""
echo "============================================"
echo "✅  TROVIA is ready!"
echo ""
echo "  Start server:  python manage.py runserver --settings=trovia.settings.dev"
echo "  Visit:         http://127.0.0.1:8000"
echo "  Admin:         http://127.0.0.1:8000/admin"
echo "    Troey:  troey@trovia.co.ke  / Trovia@2024!"
echo "    Silvia: silvia@trovia.co.ke / Trovia@2024!"
echo "============================================"
echo ""
