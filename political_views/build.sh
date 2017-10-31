#!/bin/bash

echo "Processing Political views."

## Clean
rm    -rf ./_Output
mkdir -p  ./_Output

## Copy content
cp index.html ./_Output/index.html
