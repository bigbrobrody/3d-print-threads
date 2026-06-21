# 3d-print-threads

Fusion 360 add-in that installs **3D-print-friendly metric thread definitions** with built-in clearance classes from **0.0mm to 1.0mm in 0.1mm steps**.

## What this provides

- Fusion 360 add-in button: **Install 3D Print Threads**
- Two custom thread libraries:
  - **3D Print Metric profile** — standard 60° V-thread with 3D-print clearances
  - **3D Print Metric Rounded profile** — 90° included-angle thread that limits overhang to 45° for support-free FDM printing
- Tolerance/clearance classes (both profiles):
  - `3DP-0.0mm`
  - `3DP-0.1mm`
  - `...`
  - `3DP-1.0mm`

These classes are selectable in Fusion 360's standard Thread command after installation.

## Rounded thread profile

The **3D Print Metric Rounded profile** uses a 90° included angle (45° per flank) instead of the standard 60°. This means every flank surface overhangs at exactly 45° from horizontal — the commonly accepted limit for FDM printing without support structures. The trade-off is a shallower thread depth (50% of standard metric height), so use an appropriate clearance class to ensure a good fit.

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

1. Copy `/home/runner/work/3d-print-threads/3d-print-threads/Fusion360/3DPrintThreads` into your Fusion 360 AddIns directory (%appdata%\Autodesk\FusionAddins).
2. In Fusion 360, open **Utilities → Add-Ins → Scripts and Add-Ins**.
3. Run **3DPrintThreads**.
4. Click **Install 3D Print Threads** in the Solid/Create panel.
5. Restart Fusion 360.

The add-in writes all XML thread profile files into Fusion's user `ThreadData` folder, including Windows `API\ThreadData` and webdeploy `Configuration\ThreadData` locations.

## Use

### Standard threads

1. Open Fusion 360's Thread command on a cylindrical face.
2. Set thread type to **3D Print Metric profile**.
3. Choose your thread size/designation.
4. Select thread class `3DP-<tolerance>` where tolerance is from `0.0mm` to `1.0mm`.

### Rounded threads (overhang-optimised)

1. Open Fusion 360's Thread command on a cylindrical face.
2. Set thread type to **3D Print Metric Rounded profile**.
3. Choose your thread size/designation.
4. Select thread class `3DP-<tolerance>` where tolerance is from `0.0mm` to `1.0mm`.
