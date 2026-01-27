# Show available commands
list:
    @just --list

# Generate project using defaults
bake BAKE_OPTIONS="--no-input":  
    cookiecutter {{BAKE_OPTIONS}} . --overwrite-if-exists

# Remove the boilerplate project
clean:
    rm -rf stellar-boilerplate

# Watch for changes
watch BAKE_OPTIONS="--no-input": bake
    watchmedo shell-command \
        -p '*.*' \
        -c 'just bake {{BAKE_OPTIONS}}' \
        -W -R -D {{'{{cookiecutter.project_slug}}'}}
