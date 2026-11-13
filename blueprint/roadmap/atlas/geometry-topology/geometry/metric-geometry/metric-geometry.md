---
declaration: section
origin: cited
lean: MathlibExt.Geometry.Euclidean.JohnsonLindenstraussWanted.johnson_lindenstrauss, MathlibExt.Analysis.MicroscopicWeightingWanted.microscopicWeightingIff_refuted, MathlibExt.Geometry.ScottishBook3Wanted.noCompactSetCongruentToProperSubset
statement: formalized
---

# Metric geometry: its own results

3 results, 1 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/index.html).

Geometry of general metric spaces: curvature bounds via comparison, length spaces, isometric embeddings and low-distortion embeddings.

## Johnson–Lindenstrauss lemma

There is a constant $C > 0$ with the following property. Let
$\varepsilon > 0$, let $m$ and $N \ge 2$ be natural numbers, let $X$ be a set of exactly $N$
points of $\mathbb{R}^m$ with the Euclidean norm, and let $d$ be a natural number with
$d > C \varepsilon^{-2} \log N$. Then there is a map $f : \mathbb{R}^m \to \mathbb{R}^d$ such
that $(1 - \varepsilon) \|x - y\| \le \|f(x) - f(y)\| \le (1 + \varepsilon) \|x - y\|$ for all
$x, y \in X$, where $\mathbb{R}^d$ also carries the Euclidean norm.

The map $f$ is not required to be linear, and $\varepsilon \ge 1$ is allowed (there the zero
map works). The proof takes $C = 64$ and uses a Gaussian random projection with a union bound
over pairs of points.

## Sources

- W. B. Johnson and J. Lindenstrauss, "Extensions of Lipschitz mappings into a Hilbert space," Contemporary Mathematics 26, Conference on Modern Analysis and Probability, American Mathematical Society (1984), 189--206, DOI 10.1090/conm/026/737400. ATLAS source-to-API map, item N147; ATLAS adds the hypothesis that N is at least 2.

Formalized by `MathlibExt.Geometry.Euclidean.JohnsonLindenstraussWanted.johnson_lindenstrauss`, a theorem declared in [MathlibExt/Geometry/Euclidean/JohnsonLindenstrauss.lean, line 648](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/JohnsonLindenstrauss.lean#L648). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/index.html#johnson-lindenstrauss).

## Microscopic weighting is not equivalent to finite concentration

It is not true that every
nonempty finite metric space $X$ has a microscopic weighting if and only if it has finite
concentration. Here, for real $t$, $Z_t$ is the $X \times X$ matrix with entries
$e^{-t\,d(x,y)}$ and $w_t = Z_t^{-1}\mathbf{1}$ is its weighting, where $\mathbf{1}$ is the
all-ones vector and the inverse of a singular matrix is taken to be $0$. The space $X$ has a
microscopic weighting if $w_t$ converges to some $w \colon X \to \mathbb{R}$ as $t \to 0^+$. It
has finite concentration if there are $g \colon X \to \mathbb{R}$ with $\sum_{x \in X} g(x) = 1$
and $c \in \mathbb{R}$ such that $\sum_{y \in X} d(x,y)\,g(y) = c$ for every $x \in X$.

Kenta Kitamura (assisted by ChatGPT) gave an explicit 10-point metric space with finite
concentration but no microscopic weighting.

## Sources

- Kenta Kitamura, microscopic-weighting-counterexample, Lean formalization of the 10-point counterexample, https://github.com/KitaKen1/microscopic-weighting-counterexample/blob/eff8979/lean/MicroscopicWeightingCounterexampleFC.lean#L886-L894.

Stated but not proved: `MathlibExt.Analysis.MicroscopicWeightingWanted.microscopicWeightingIff_refuted` is written with `theorem_wanted` in [WantedExt/Analysis/MicroscopicWeightingWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/MicroscopicWeightingWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/index.html#microscopic-weighting-iff-refuted).

## No compact set is congruent to a proper subset of itself

Let $K$ be a compact subset of
a metric space $X$. Then there is no map $f : X \to X$ with $d(f(x), f(y)) = d(x, y)$ for all
$x, y \in X$ such that $f(K) \subseteq K$ and $f(K) \neq K$.

The underlying fact is that an isometric embedding of a compact metric space into itself is
surjective.

## Sources

- S. Banach and S. Ulam, Problem 3 of the Scottish Book, stated and proved in the Scottish Book typescript.

Stated but not proved: `MathlibExt.Geometry.ScottishBook3Wanted.noCompactSetCongruentToProperSubset` is written with `theorem_wanted` in [WantedExt/Geometry/ScottishBook3Wanted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/ScottishBook3Wanted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/index.html#no-compact-set-congruent-to-proper-subse).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Metric geometry](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/metric-geometry)
