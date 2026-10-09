---
title: File Transfers from Biowulf
author: "[Vishal Koparde](https://github.com/kopardev)"
---

> 🛑 **STOP**: File transfers must go through HELIX. Do not start transfers from Biowulf.
>
> `dm_register_dataobject_multipart` is not supported from Biowulf, and the supported workflow is to transfer files from HELIX instead. See [File Transfer from HELIX](transferFromHelix.md) for the correct procedure.

## Short answer

If you need to move data to HPC-DME, do this:

1. Log in to HELIX.
2. Run the supported transfer workflow from HELIX.
3. Do not use Biowulf for the transfer step.

## Why this is required

The Biowulf-side multipart transfer path is currently not working. Use HELIX as the supported transfer host for HPC-DME archiving and backup workflows.

## Follow the HELIX guide

Use the HELIX workflow here:

- [File Transfer from HELIX](transferFromHelix.md)

This is the supported path for managing HPC-DME transfers.
