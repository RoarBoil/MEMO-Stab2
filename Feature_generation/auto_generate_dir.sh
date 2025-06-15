#!/bin/bash

# 指定目标目录
TARGET_DIR="./features" # todo

# 创建子目录
mkdir -p "$TARGET_DIR/esm2"
mkdir -p "$TARGET_DIR/fasta"
mkdir -p "$TARGET_DIR/fasta_split"
mkdir -p "$TARGET_DIR/hhblits"
mkdir -p "$TARGET_DIR/netSurfP"
mkdir -p "$TARGET_DIR/protT5"
mkdir -p "$TARGET_DIR/slurms"
mkdir -p "$TARGET_DIR/temp_sh"


mkdir -p "$TARGET_DIR/esm2/point_representations_after"
mkdir -p "$TARGET_DIR/esm2/point_representations_before"
mkdir -p "$TARGET_DIR/esm2/sequence_representations_after"
mkdir -p "$TARGET_DIR/esm2/sequence_representations_before"

mkdir -p "$TARGET_DIR/fasta/after"
mkdir -p "$TARGET_DIR/fasta/before"

mkdir -p "$TARGET_DIR/fasta_split/after"
mkdir -p "$TARGET_DIR/fasta_split/before"

mkdir -p "$TARGET_DIR/protT5/point_representations_after"
mkdir -p "$TARGET_DIR/protT5/point_representations_before"
mkdir -p "$TARGET_DIR/protT5/sequence_representations_after"
mkdir -p "$TARGET_DIR/protT5/sequence_representations_before"

echo "子目录已成功创建在 $TARGET_DIR"