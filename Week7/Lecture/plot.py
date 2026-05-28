"""
Matplotlib Plot Types - Comprehensive Demo
==========================================
Covers all major plot types available in matplotlib.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
import numpy as np

# ── Shared random seed for reproducibility ────────────────────────────────────
rng = np.random.default_rng(42)

# ═══════════════════════════════════════════════════════════════════════════════
# 1. LINE PLOT
# ═══════════════════════════════════════════════════════════════════════════════
x = np.linspace(0, 2 * np.pi, 200)

fig, ax = plt.subplots()
ax.plot(x, np.sin(x), label="sin(x)")
ax.plot(x, np.cos(x), label="cos(x)", linestyle="--")
ax.set_title("1. Line Plot")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
plt.tight_layout()
plt.savefig("01_line_plot.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 2. SCATTER PLOT
# ═══════════════════════════════════════════════════════════════════════════════
n = 100
x_s = rng.standard_normal(n)
y_s = 2 * x_s + rng.standard_normal(n)
colors = rng.random(n)
sizes  = rng.integers(20, 200, n)

fig, ax = plt.subplots()
sc = ax.scatter(x_s, y_s, c=colors, s=sizes, cmap="viridis", alpha=0.7)
plt.colorbar(sc, ax=ax, label="Random color value")
ax.set_title("2. Scatter Plot")
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.tight_layout()
plt.savefig("02_scatter_plot.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 3. BAR CHART  (vertical)
# ═══════════════════════════════════════════════════════════════════════════════
categories = ["Mon", "Tue", "Wed", "Thu", "Fri"]
values     = [23, 45, 12, 67, 34]

fig, ax = plt.subplots()
bars = ax.bar(categories, values, color="steelblue", edgecolor="black")
ax.bar_label(bars, padding=3)
ax.set_title("3. Bar Chart (Vertical)")
ax.set_ylabel("Sales")
plt.tight_layout()
plt.savefig("03_bar_chart.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 4. HORIZONTAL BAR CHART
# ═══════════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots()
bars = ax.barh(categories, values, color="coral", edgecolor="black")
ax.bar_label(bars, padding=3)
ax.set_title("4. Horizontal Bar Chart")
ax.set_xlabel("Sales")
plt.tight_layout()
plt.savefig("04_barh_chart.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 5. GROUPED BAR CHART
# ═══════════════════════════════════════════════════════════════════════════════
quarters  = ["Q1", "Q2", "Q3", "Q4"]
product_a = [30, 50, 70, 90]
product_b = [20, 40, 60, 80]
product_c = [10, 30, 50, 70]

x_pos = np.arange(len(quarters))
width = 0.25

fig, ax = plt.subplots()
ax.bar(x_pos - width, product_a, width, label="Product A", color="steelblue")
ax.bar(x_pos,         product_b, width, label="Product B", color="coral")
ax.bar(x_pos + width, product_c, width, label="Product C", color="seagreen")
ax.set_xticks(x_pos)
ax.set_xticklabels(quarters)
ax.set_title("5. Grouped Bar Chart")
ax.set_ylabel("Revenue (k€)")
ax.legend()
plt.tight_layout()
plt.savefig("05_grouped_bar.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 6. STACKED BAR CHART
# ═══════════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots()
ax.bar(quarters, product_a, label="Product A", color="steelblue")
ax.bar(quarters, product_b, bottom=product_a, label="Product B", color="coral")
bottom_ab = [a + b for a, b in zip(product_a, product_b)]
ax.bar(quarters, product_c, bottom=bottom_ab, label="Product C", color="seagreen")
ax.set_title("6. Stacked Bar Chart")
ax.set_ylabel("Revenue (k€)")
ax.legend()
plt.tight_layout()
plt.savefig("06_stacked_bar.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 7. HISTOGRAM
# ═══════════════════════════════════════════════════════════════════════════════
data = rng.normal(loc=50, scale=10, size=1000)

fig, ax = plt.subplots()
ax.hist(data, bins=30, color="steelblue", edgecolor="black", alpha=0.7)
ax.set_title("7. Histogram")
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")
plt.tight_layout()
plt.savefig("07_histogram.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 8. STACKED HISTOGRAM
# ═══════════════════════════════════════════════════════════════════════════════
data1 = rng.normal(40, 10, 500)
data2 = rng.normal(60, 10, 500)

fig, ax = plt.subplots()
ax.hist([data1, data2], bins=25, stacked=True,
        color=["steelblue", "coral"], label=["Group A", "Group B"],
        edgecolor="black", alpha=0.8)
ax.set_title("8. Stacked Histogram")
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")
ax.legend()
plt.tight_layout()
plt.savefig("08_stacked_histogram.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 9. PIE CHART
# ═══════════════════════════════════════════════════════════════════════════════
slices = [35, 25, 20, 15, 5]
labels = ["Python", "Java", "C++", "JavaScript", "Others"]
explode = [0.05] * len(slices)

fig, ax = plt.subplots()
ax.pie(slices, labels=labels, explode=explode, autopct="%1.1f%%",
       startangle=140, shadow=True)
ax.set_title("9. Pie Chart — Programming Languages")
plt.tight_layout()
plt.savefig("09_pie_chart.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 10. DONUT CHART
# ═══════════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(
    slices, labels=labels, autopct="%1.1f%%",
    wedgeprops=dict(width=0.5), startangle=140
)
ax.set_title("10. Donut Chart")
plt.tight_layout()
plt.savefig("10_donut_chart.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 11. BOX PLOT
# ═══════════════════════════════════════════════════════════════════════════════
box_data = [rng.normal(loc, 1, 100) for loc in [1, 2, 3, 4, 5]]

fig, ax = plt.subplots()
ax.boxplot(box_data, labels=["A", "B", "C", "D", "E"], patch_artist=True,
           boxprops=dict(facecolor="lightblue"))
ax.set_title("11. Box Plot")
ax.set_xlabel("Group")
ax.set_ylabel("Value")
plt.tight_layout()
plt.savefig("11_box_plot.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 12. VIOLIN PLOT
# ═══════════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots()
parts = ax.violinplot(box_data, positions=[1, 2, 3, 4, 5], showmedians=True)
for pc in parts["bodies"]:
    pc.set_facecolor("lightblue")
    pc.set_alpha(0.7)
ax.set_title("12. Violin Plot")
ax.set_xlabel("Group")
ax.set_ylabel("Value")
plt.tight_layout()
plt.savefig("12_violin_plot.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 13. AREA PLOT (fill_between)
# ═══════════════════════════════════════════════════════════════════════════════
x_a = np.linspace(0, 10, 300)
y1  = np.sin(x_a) + 2
y2  = np.cos(x_a) + 2

fig, ax = plt.subplots()
ax.fill_between(x_a, y1, alpha=0.5, label="sin(x)+2", color="steelblue")
ax.fill_between(x_a, y2, alpha=0.5, label="cos(x)+2", color="coral")
ax.set_title("13. Area Plot (fill_between)")
ax.legend()
plt.tight_layout()
plt.savefig("13_area_plot.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 14. STEP PLOT
# ═══════════════════════════════════════════════════════════════════════════════
x_step = np.arange(10)
y_step = rng.integers(1, 10, 10)

fig, ax = plt.subplots()
ax.step(x_step, y_step, where="mid", color="steelblue", linewidth=2)
ax.set_title("14. Step Plot")
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.tight_layout()
plt.savefig("14_step_plot.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 15. STEM PLOT
# ═══════════════════════════════════════════════════════════════════════════════
x_stem = np.linspace(0, 2 * np.pi, 20)
y_stem = np.sin(x_stem)

fig, ax = plt.subplots()
ax.stem(x_stem, y_stem)
ax.set_title("15. Stem Plot")
ax.set_xlabel("x")
ax.set_ylabel("sin(x)")
plt.tight_layout()
plt.savefig("15_stem_plot.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 16. ERROR BAR PLOT
# ═══════════════════════════════════════════════════════════════════════════════
x_e = np.arange(1, 6)
y_e = [2.1, 3.5, 2.8, 4.2, 3.9]
y_err = [0.3, 0.5, 0.2, 0.4, 0.6]

fig, ax = plt.subplots()
ax.errorbar(x_e, y_e, yerr=y_err, fmt="o-", capsize=5,
            color="steelblue", ecolor="red", linewidth=2)
ax.set_title("16. Error Bar Plot")
ax.set_xlabel("x")
ax.set_ylabel("Measurement")
plt.tight_layout()
plt.savefig("16_errorbar_plot.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 17. HEATMAP (imshow)
# ═══════════════════════════════════════════════════════════════════════════════
matrix = rng.random((10, 10))

fig, ax = plt.subplots()
im = ax.imshow(matrix, cmap="hot", interpolation="nearest")
plt.colorbar(im, ax=ax)
ax.set_title("17. Heatmap (imshow)")
plt.tight_layout()
plt.savefig("17_heatmap.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 18. CONTOUR PLOT
# ═══════════════════════════════════════════════════════════════════════════════
X, Y = np.meshgrid(np.linspace(-3, 3, 200), np.linspace(-3, 3, 200))
Z    = np.sin(X) * np.cos(Y)

fig, ax = plt.subplots()
cs = ax.contour(X, Y, Z, levels=15, cmap="RdYlBu")
ax.clabel(cs, inline=True, fontsize=8)
ax.set_title("18. Contour Plot")
plt.tight_layout()
plt.savefig("18_contour_plot.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 19. FILLED CONTOUR PLOT
# ═══════════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots()
cf = ax.contourf(X, Y, Z, levels=20, cmap="RdYlBu")
plt.colorbar(cf, ax=ax)
ax.set_title("19. Filled Contour Plot (contourf)")
plt.tight_layout()
plt.savefig("19_contourf_plot.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 20. 3-D LINE PLOT
# ═══════════════════════════════════════════════════════════════════════════════
t   = np.linspace(0, 4 * np.pi, 300)
x3  = np.sin(t)
y3  = np.cos(t)
z3  = t / (4 * np.pi)

fig = plt.figure()
ax  = fig.add_subplot(111, projection="3d")
ax.plot(x3, y3, z3, color="steelblue")
ax.set_title("20. 3-D Line Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.tight_layout()
plt.savefig("20_3d_line.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 21. 3-D SCATTER PLOT
# ═══════════════════════════════════════════════════════════════════════════════
xs = rng.standard_normal(100)
ys = rng.standard_normal(100)
zs = rng.standard_normal(100)

fig = plt.figure()
ax  = fig.add_subplot(111, projection="3d")
ax.scatter(xs, ys, zs, c=zs, cmap="plasma", s=40)
ax.set_title("21. 3-D Scatter Plot")
plt.tight_layout()
plt.savefig("21_3d_scatter.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 22. 3-D SURFACE PLOT
# ═══════════════════════════════════════════════════════════════════════════════
X3, Y3 = np.meshgrid(np.linspace(-3, 3, 60), np.linspace(-3, 3, 60))
Z3     = np.sin(np.sqrt(X3**2 + Y3**2))

fig = plt.figure()
ax  = fig.add_subplot(111, projection="3d")
surf = ax.plot_surface(X3, Y3, Z3, cmap="viridis", alpha=0.85)
plt.colorbar(surf, ax=ax, shrink=0.5)
ax.set_title("22. 3-D Surface Plot")
plt.tight_layout()
plt.savefig("22_3d_surface.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 23. 3-D WIREFRAME PLOT
# ═══════════════════════════════════════════════════════════════════════════════
fig = plt.figure()
ax  = fig.add_subplot(111, projection="3d")
ax.plot_wireframe(X3, Y3, Z3, rstride=5, cstride=5, color="steelblue")
ax.set_title("23. 3-D Wireframe Plot")
plt.tight_layout()
plt.savefig("23_3d_wireframe.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 24. POLAR PLOT
# ═══════════════════════════════════════════════════════════════════════════════
theta  = np.linspace(0, 2 * np.pi, 300)
r_rose = np.abs(np.sin(3 * theta))   # 3-petal rose

fig, ax = plt.subplots(subplot_kw={"projection": "polar"})
ax.plot(theta, r_rose, color="crimson")
ax.fill(theta, r_rose, alpha=0.2, color="crimson")
ax.set_title("24. Polar Plot (Rose Curve)", va="bottom")
plt.tight_layout()
plt.savefig("24_polar_plot.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 25. RADAR / SPIDER CHART
# ═══════════════════════════════════════════════════════════════════════════════
skills  = ["Python", "Statistics", "ML", "SQL", "Visualization", "Communication"]
n_skills = len(skills)
values_radar = [8, 7, 9, 6, 8, 7]
values_radar += values_radar[:1]          # close the polygon

angles = [n / float(n_skills) * 2 * np.pi for n in range(n_skills)]
angles += angles[:1]

fig, ax = plt.subplots(subplot_kw={"projection": "polar"})
ax.plot(angles, values_radar, "o-", linewidth=2, color="steelblue")
ax.fill(angles, values_radar, alpha=0.25, color="steelblue")
ax.set_xticks(angles[:-1])
ax.set_xticklabels(skills, size=9)
ax.set_ylim(0, 10)
ax.set_title("25. Radar / Spider Chart", va="bottom")
plt.tight_layout()
plt.savefig("25_radar_chart.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 26. QUIVER PLOT (vector field)
# ═══════════════════════════════════════════════════════════════════════════════
xq, yq = np.meshgrid(np.linspace(-2, 2, 12), np.linspace(-2, 2, 12))
U = -yq
V =  xq

fig, ax = plt.subplots()
ax.quiver(xq, yq, U, V, np.sqrt(U**2 + V**2), cmap="plasma")
ax.set_title("26. Quiver Plot (Vector Field)")
ax.set_aspect("equal")
plt.tight_layout()
plt.savefig("26_quiver_plot.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 27. STREAM PLOT
# ═══════════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots()
ax.streamplot(xq[0], yq[:, 0], U, V,
              color=np.sqrt(U**2 + V**2), cmap="plasma", density=1.2)
ax.set_title("27. Stream Plot")
plt.tight_layout()
plt.savefig("27_stream_plot.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 28. 2-D HISTOGRAM  (hist2d)
# ═══════════════════════════════════════════════════════════════════════════════
x_h = rng.standard_normal(5000)
y_h = x_h + rng.standard_normal(5000)

fig, ax = plt.subplots()
h, xedges, yedges, img = ax.hist2d(x_h, y_h, bins=40, cmap="YlOrRd")
plt.colorbar(img, ax=ax, label="Count")
ax.set_title("28. 2-D Histogram (hist2d)")
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.tight_layout()
plt.savefig("28_hist2d.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 29. HEX-BIN PLOT
# ═══════════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots()
hb = ax.hexbin(x_h, y_h, gridsize=30, cmap="inferno")
plt.colorbar(hb, ax=ax, label="Count")
ax.set_title("29. Hex-Bin Plot")
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.tight_layout()
plt.savefig("29_hexbin_plot.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 30. BROKEN BARH (Gantt-style)
# ═══════════════════════════════════════════════════════════════════════════════
tasks  = ["Research", "Design", "Coding", "Testing", "Deploy"]
starts = [0, 2, 4, 7, 9]
durations = [3, 3, 4, 2, 2]
colors_g = ["steelblue", "coral", "seagreen", "goldenrod", "orchid"]

fig, ax = plt.subplots(figsize=(8, 3))
for i, (task, start, dur, col) in enumerate(zip(tasks, starts, durations, colors_g)):
    ax.broken_barh([(start, dur)], (i - 0.4, 0.8), facecolors=col)
ax.set_yticks(range(len(tasks)))
ax.set_yticklabels(tasks)
ax.set_xlabel("Week")
ax.set_title("30. Broken Barh — Gantt Chart")
plt.tight_layout()
plt.savefig("30_broken_barh.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 31. ANNOTATED PLOT
# ═══════════════════════════════════════════════════════════════════════════════
x_an = np.linspace(0, 2 * np.pi, 200)
y_an = np.sin(x_an)

fig, ax = plt.subplots()
ax.plot(x_an, y_an)
max_x = x_an[np.argmax(y_an)]
max_y = y_an.max()
ax.annotate(
    f"Max = {max_y:.2f}",
    xy=(max_x, max_y),
    xytext=(max_x + 0.5, max_y - 0.3),
    arrowprops=dict(arrowstyle="->", color="red"),
    fontsize=10, color="red"
)
ax.set_title("31. Annotated Plot")
plt.tight_layout()
plt.savefig("31_annotated_plot.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 32. TWIN AXES (dual y-axis)
# ═══════════════════════════════════════════════════════════════════════════════
x_tw = np.linspace(0, 10, 100)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(x_tw, np.sin(x_tw), color="steelblue", label="sin(x)")
ax2.plot(x_tw, np.exp(x_tw * 0.3), color="coral", linestyle="--", label="exp(0.3x)")
ax1.set_xlabel("x")
ax1.set_ylabel("sin(x)", color="steelblue")
ax2.set_ylabel("exp(0.3x)", color="coral")
ax1.set_title("32. Twin Axes (Dual Y-Axis)")
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")
plt.tight_layout()
plt.savefig("32_twin_axes.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 33. SUBPLOTS GRID (overview panel)
# ═══════════════════════════════════════════════════════════════════════════════
fig, axes = plt.subplots(2, 3, figsize=(12, 7))
axes = axes.flatten()

# Panel data
x_p = np.linspace(0, 2 * np.pi, 100)
panel_plots = [
    (lambda ax: ax.plot(x_p, np.sin(x_p)),           "sin(x)"),
    (lambda ax: ax.bar(["A", "B", "C"], [3, 7, 5]),  "Bar"),
    (lambda ax: ax.scatter(rng.random(30), rng.random(30)), "Scatter"),
    (lambda ax: ax.hist(rng.normal(0, 1, 500), bins=20), "Histogram"),
    (lambda ax: ax.pie([40, 30, 20, 10], labels=["W","X","Y","Z"], autopct="%1.0f%%"), "Pie"),
    (lambda ax: ax.imshow(rng.random((8, 8)), cmap="viridis"), "Heatmap"),
]
for (fn, title), ax in zip(panel_plots, axes):
    fn(ax)
    ax.set_title(title)

fig.suptitle("33. Subplots Grid — Quick Overview", fontsize=14)
plt.tight_layout()
plt.savefig("33_subplots_grid.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 34. LOG-SCALE PLOT
# ═══════════════════════════════════════════════════════════════════════════════
x_log = np.logspace(0, 4, 100)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].plot(x_log, x_log ** 2)
axes[0].set_title("Linear Scale")
axes[1].loglog(x_log, x_log ** 2, color="crimson")
axes[1].set_title("Log-Log Scale")
for ax in axes:
    ax.set_xlabel("x")
    ax.set_ylabel("x²")
fig.suptitle("34. Log-Scale Plot")
plt.tight_layout()
plt.savefig("34_log_scale.png", dpi=100)
plt.show()

# ═══════════════════════════════════════════════════════════════════════════════
# 35. CANDLESTICK-STYLE  (using bar + vlines)
# ═══════════════════════════════════════════════════════════════════════════════
days  = np.arange(1, 11)
opens = rng.uniform(100, 110, 10)
closes= opens + rng.uniform(-5, 5, 10)
highs = np.maximum(opens, closes) + rng.uniform(0, 3, 10)
lows  = np.minimum(opens, closes) - rng.uniform(0, 3, 10)
colors_c = ["seagreen" if c > o else "crimson" for o, c in zip(opens, closes)]

fig, ax = plt.subplots()
ax.bar(days, np.abs(closes - opens), bottom=np.minimum(opens, closes),
       color=colors_c, width=0.6)
ax.vlines(days, lows, highs, color="black", linewidth=1)
ax.set_title("35. Candlestick-Style Chart")
ax.set_xlabel("Day")
ax.set_ylabel("Price")
plt.tight_layout()
plt.savefig("35_candlestick_style.png", dpi=100)
plt.show()

print("\nAll plots saved as PNG files in the current directory.")
