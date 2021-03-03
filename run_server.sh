#!/usr/bin/bash
gunicorn -b '0.0.0.0':'8005' --workers=4 'aocAPI:create_app()'