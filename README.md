# 3d-print-threads

Fusion 360 add-in that installs **3D-print-friendly metric thread definitions** with built-in clearance classes from **0.0mm to 1.0mm in 0.1mm steps**.

## What this provides

- Fusion 360 add-in button: **Install 3D Print Threads**
- Custom thread library: **3D Print Metric profile**
- Tolerance/clearance classes:
  - `3DP-0.0mm`
  - `3DP-0.1mm`
  - `...`
  - `3DP-1.0mm`

These classes are selectable in Fusion 360's standard Thread command after installation.

## Included thread sizes

- M3x0.5
- M4x0.7
- M5x0.8
- M6x1.0
- M8x1.25
- M10x1.5
- M12x1.75
- M16x2.0
- M20x2.5

## Install

1. Copy `/home/runner/work/3d-print-threads/3d-print-threads/Fusion360/3DPrintThreads` into your Fusion 360 AddIns directory.
2. In Fusion 360, open **Utilities → Add-Ins → Scripts and Add-Ins**.
3. Run **3DPrintThreads**.
4. Click **Install 3D Print Threads** in the Solid/Create panel.
5. Restart Fusion 360.

The add-in writes `3DPrintMetric.xml` into Fusion's user `ThreadData` folder.

## Use

1. Open Fusion 360's Thread command on a cylindrical face.
2. Set thread type to **3D Print Metric profile**.
3. Choose your thread size/designation.
4. Select thread class `3DP-<tolerance>` where tolerance is from `0.0mm` to `1.0mm`.
