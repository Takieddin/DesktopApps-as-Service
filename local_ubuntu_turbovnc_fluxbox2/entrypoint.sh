#!/bin/bash
set -ex



exec supervisord -c supervisord.conf
