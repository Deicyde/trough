---
declaration: section
origin: cited
lean: Isometries.Plane, Isometries.linearDet, Isometries.IsTranslation, Isometries.IsRotation, Isometries.IsReflection, Isometries.IsGlideReflection, Isometries.plane_isometry_classification
statement: formalized
proof: formalized
---

# Classification of plane isometries

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/classification-of-plane-isometries/index.html).

## The Euclidean plane

The Euclidean plane is the real vector space $\mathbb{R}^2$ with
its standard inner product $\langle x, y \rangle = x_1 y_1 + x_2 y_2$.

Formalized by `Isometries.Plane`, an abbreviation declared in [MathlibExt/Geometry/Euclidean/PlaneIsometryClassification.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/PlaneIsometryClassification.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/classification-of-plane-isometries/index.html#plane).

## Linear determinant of a plane isometry

The linear determinant of an isometry $f$ of
the Euclidean plane is the determinant of the linear part of $f$.

Formalized by `Isometries.linearDet`, a definition declared in [MathlibExt/Geometry/Euclidean/PlaneIsometryClassification.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/PlaneIsometryClassification.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/classification-of-plane-isometries/index.html#linear-det).

## Translation

An isometry $f$ of the Euclidean plane is a translation if there is a
vector $v$ such that $f(x) = x + v$ for every point $x$.

Formalized by `Isometries.IsTranslation`, a definition declared in [MathlibExt/Geometry/Euclidean/PlaneIsometryClassification.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/PlaneIsometryClassification.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/classification-of-plane-isometries/index.html#is-translation).

## Rotation

An isometry $f$ of the Euclidean plane is a rotation if it fixes some point
$p$, the determinant of its linear part is $1$, and $f$ is not a translation.

Formalized by `Isometries.IsRotation`, a definition declared in [MathlibExt/Geometry/Euclidean/PlaneIsometryClassification.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/PlaneIsometryClassification.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/classification-of-plane-isometries/index.html#is-rotation).

## Reflection

An isometry $f$ of the Euclidean plane is a reflection if there is a line
$L$ such that $f(x) = x$ for every point $x$ of $L$, and the determinant of the linear part
of $f$ is $-1$.

Formalized by `Isometries.IsReflection`, a definition declared in [MathlibExt/Geometry/Euclidean/PlaneIsometryClassification.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/PlaneIsometryClassification.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/classification-of-plane-isometries/index.html#is-reflection).

## Glide reflection

An isometry $f$ of the Euclidean plane is a glide reflection if the
determinant of its linear part is $-1$ and there are a line $L$ and a nonzero vector $v$
parallel to $L$ such that $f(x) = x + v$ for every point $x$ of $L$.

Formalized by `Isometries.IsGlideReflection`, a definition declared in [MathlibExt/Geometry/Euclidean/PlaneIsometryClassification.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/PlaneIsometryClassification.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/classification-of-plane-isometries/index.html#is-glide-reflection).

## Classification of plane isometries

Every isometry of the Euclidean
plane is a translation, a rotation, a reflection, or a glide reflection.

Formalized by `Isometries.plane_isometry_classification`, a theorem declared in [MathlibExt/Geometry/Euclidean/PlaneIsometryClassification.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/PlaneIsometryClassification.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/classification-of-plane-isometries/index.html#plane-isometry-classification).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Classification of plane isometries](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/classification-of-plane-isometries/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/classification-of-plane-isometries)
