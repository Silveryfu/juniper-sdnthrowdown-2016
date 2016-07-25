#!/bin/bash

$(which time) --format='%C took %e seconds' ./install.sh
$(which time) --format='%C took %e seconds' ./start.sh
