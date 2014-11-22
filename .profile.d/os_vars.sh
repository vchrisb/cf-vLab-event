#!/bin/sh
export NEW_RELIC_LICENSE_KEY="$(python $HOME/.profile.d/newrelic_license.py)"
export NEW_RELIC_APP_NAME="$(python $HOME/.profile.d/app_name.py)"