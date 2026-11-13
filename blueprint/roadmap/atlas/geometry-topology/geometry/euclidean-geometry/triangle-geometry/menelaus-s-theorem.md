---
declaration: section
origin: cited
lean: MetaMathlibExt.menelaus_general, MetaMathlibExt.menelaus
statement: formalized
proof: formalized
---

# Menelaus's theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/menelaus-s-theorem/index.html).

## Menelaus's theorem, general form

Let $A$, $B$, $C$ be points of the Euclidean plane
$\mathbb{R}^2$ with $A \ne B$ and $C$ not on the line $AB$. Let $D$, $E$, $F$ be points and
let $\alpha, \alpha', \beta, \beta', \gamma, \gamma'$ be real numbers with
$F - A = \alpha (B - A)$, $B - F = \alpha' (B - A)$, $D - B = \beta (C - B)$,
$C - D = \beta' (C - B)$, $E - C = \gamma (A - C)$, $A - E = \gamma' (A - C)$, and
$\alpha', \beta', \gamma' \ne 0$. Then $F$ lies on the line through $D$ and $E$ if and only if
$\frac{\alpha}{\alpha'} \cdot \frac{\beta}{\beta'} \cdot \frac{\gamma}{\gamma'} = -1$.

The numbers $\alpha, \alpha', \beta, \beta', \gamma, \gamma'$ are the signed ratios $AF/AB$,
$FB/AB$, $BD/BC$, $DC/BC$, $CE/CA$, $EA/CA$, so the product is the classical signed ratio
product $\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA}$.

Formalized by `MetaMathlibExt.menelaus_general`, a theorem declared in [MathlibExt/Geometry/Euclidean/Menelaus.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/Menelaus.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/menelaus-s-theorem/index.html#menelaus-general).

## Menelaus's theorem

Let $A$, $B$, $C$ be pairwise distinct points of the Euclidean plane
$\mathbb{R}^2$ with $C$ not on the line $AB$. Let $D$, $E$, $F$ be points on the lines $BC$, $CA$
and $AB$ respectively, with $D \ne B$, $D \ne C$, $E \ne C$, $E \ne A$, $F \ne A$ and $F \ne B$.
Let $\alpha, \alpha', \beta, \beta', \gamma, \gamma'$ be real numbers with
$F - A = \alpha (B - A)$, $B - F = \alpha' (B - A)$, $D - B = \beta (C - B)$,
$C - D = \beta' (C - B)$, $E - C = \gamma (A - C)$, $A - E = \gamma' (A - C)$, and
$\alpha', \beta', \gamma' \ne 0$. Then $F$ lies on the line through $D$ and $E$ if and only if
$\frac{\alpha}{\alpha'} \cdot \frac{\beta}{\beta'} \cdot \frac{\gamma}{\gamma'} = -1$.

The numbers $\alpha, \alpha', \beta, \beta', \gamma, \gamma'$ are the signed ratios $AF/AB$,
$FB/AB$, $BD/BC$, $DC/BC$, $CE/CA$, $EA/CA$, so the product is the classical signed ratio
product $\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA}$. The incidence hypotheses,
$B \ne C$, $A \ne C$ and the conditions that $D$, $E$, $F$ avoid the vertices follow from the
other hypotheses or are not needed; they keep the shape of the classical statement.

## Sources

- https://en.wikipedia.org/wiki/Menelaus%27s_theorem.

Formalized by `MetaMathlibExt.menelaus`, a theorem declared in [MathlibExt/Geometry/Euclidean/Menelaus.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/Menelaus.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/menelaus-s-theorem/index.html#menelaus).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Menelaus's theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/menelaus-s-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/euclidean-geometry/triangle-geometry/menelaus-s-theorem)
