---
declaration: section
origin: cited
lean: MathlibExt.Geometry.OptimalMoebiusWanted.OptimalMoebius.unitStrip, MathlibExt.Geometry.OptimalMoebiusWanted.OptimalMoebius.period, MathlibExt.Geometry.OptimalMoebiusWanted.OptimalMoebius.fundamentalDomain, MathlibExt.Geometry.OptimalMoebiusWanted.OptimalMoebius.IsMoebiusEmbedding, MathlibExt.Geometry.OptimalMoebiusWanted.OptimalMoebius.theorem_1_1
statement: formalized
---

# Optimal paper Möbius band

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/optimal-paper-m-bius-band/index.html).

## Unit strip

The unit strip is the set of points $(x, y) \in \mathbb{R}^2$ with
$0 \le x \le 1$, that is, $[0, 1] \times \mathbb{R}$.

Formalized by `MathlibExt.Geometry.OptimalMoebiusWanted.OptimalMoebius.unitStrip`, an abbreviation declared in [WantedExt/Geometry/OptimalMoebiusWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/OptimalMoebiusWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/optimal-paper-m-bius-band/index.html#unit-strip).

## Gluing map of the Moebius band

For a real number $a$, this is the map
$\mathbb{R}^2 \to \mathbb{R}^2$ given by $(x, y) \mapsto (1 - x, y + a)$.

Formalized by `MathlibExt.Geometry.OptimalMoebiusWanted.OptimalMoebius.period`, a definition declared in [WantedExt/Geometry/OptimalMoebiusWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/OptimalMoebiusWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/optimal-paper-m-bius-band/index.html#period).

## Fundamental domain of the Moebius band

For a real number $a$, this is the set of points
$(x, y) \in \mathbb{R}^2$ with $0 \le x \le 1$ and $0 \le y < a$.

Formalized by `MathlibExt.Geometry.OptimalMoebiusWanted.OptimalMoebius.fundamentalDomain`, a definition declared in [WantedExt/Geometry/OptimalMoebiusWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/OptimalMoebiusWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/optimal-paper-m-bius-band/index.html#fundamental-domain).

## Moebius embedding

Let $a$ be a real number, let $S = [0, 1] \times \mathbb{R}$ be the
unit strip and let $f : \mathbb{R}^2 \to \mathbb{R}^3$. Then $f$ is a Moebius embedding of
aspect ratio $a$ if $f(1 - x, y + a) = f(x, y)$ for every $(x, y) \in S$, $f$ is $C^\infty$ on
$S$, at every point of $S$ the derivative of $f$ within $S$ is a linear isometry
$\mathbb{R}^2 \to \mathbb{R}^3$, and $f$ is injective on $[0, 1] \times [0, a)$.

This encodes the paper's smooth isometric embedding of a Moebius band: the strip is glued into
a band by the first condition, and injectivity on a fundamental domain makes the glued map an
embedding.

Formalized by `MathlibExt.Geometry.OptimalMoebiusWanted.OptimalMoebius.IsMoebiusEmbedding`, a structure declared in [WantedExt/Geometry/OptimalMoebiusWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/OptimalMoebiusWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/optimal-paper-m-bius-band/index.html#is-moebius-embedding).

## Schwartz's optimal paper Moebius band theorem

Let $a > 0$. If
$f : \mathbb{R}^2 \to \mathbb{R}^3$ is a Moebius embedding of aspect ratio $a$, then
$a > \sqrt{3}$. That is, a smooth embedded paper Moebius band has aspect ratio greater
than $\sqrt{3}$.

## Sources

- R. E. Schwartz, `The optimal paper Moebius band`, Annals of Math, 201 (1) 2025. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_optimal_moebius` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.OptimalMoebiusWanted.OptimalMoebius.theorem_1_1` is written with `theorem_wanted` in [WantedExt/Geometry/OptimalMoebiusWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/OptimalMoebiusWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/optimal-paper-m-bius-band/index.html#theorem-1-1).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Optimal paper Möbius band](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/optimal-paper-m-bius-band/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/curves-and-surfaces/optimal-paper-m-bius-band)
