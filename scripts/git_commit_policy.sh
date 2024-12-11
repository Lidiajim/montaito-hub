#!/bin/bash

# Solicitar tipo de commit
echo "Selecciona el tipo de commit:"
options=("feature" "fix" "docs" "test" "config" "Cancel")
select opt in "${options[@]}"
do
    case $opt in
        "feature"|"fix"|"docs"|"test"|"config")
            type=$opt
            break
            ;;
        "Cancel")
            echo "Commit cancelado."
            exit 1
            ;;
        *)
            echo "Opción no válida. Inténtalo nuevamente."
            ;;
    esac
done

# Solicitar descripción
echo "Escribe una descripción breve del commit (máx. 50 caracteres):"
read description

# Validar longitud de la descripción
if [ ${#description} -gt 50 ]; then
    echo "Error: La descripción no debe exceder los 50 caracteres."
    exit 1
fi

# Construir mensaje de commit
commit_message="$type: $description"

# Mostrar mensaje final para confirmación
echo "Mensaje de commit: \"$commit_message\""
echo "¿Deseas proceder con el commit? (y/n)"
read confirmation

if [[ $confirmation == "y" || $confirmation == "Y" ]]; then
    git add .
    git commit -m "$commit_message"
    echo "Commit realizado con éxito: $commit_message"
else
    echo "Commit cancelado."
fi
