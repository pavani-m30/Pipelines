#!/bin/bash

# Exit if any command fails
set -e

echo "===== Jenkins Java Build Script Started ====="

# Compile the Java file
javac SumExample.java

# Run the compiled class
java SumExample

echo "===== Jenkins Java Build Script Finished Successfully ====="

