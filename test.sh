#!/usr/bin/env bash
set -eu

REPO_PATH="$(dirname "$(realpath "${0}")")"

IMAGE_NAME="$(basename "${REPO_PATH}")"
IMAGE_TAG="latest"

function build () {
    pushd "${REPO_PATH}" > /dev/null
    docker build --file ./tests/Dockerfile --tag "${IMAGE_NAME}:${IMAGE_TAG}" .
    popd > /dev/null
}

function run () {
    docker run -t --rm "${IMAGE_NAME}:${IMAGE_TAG}"
}

function main () {
    build
    run
}

main
