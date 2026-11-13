---
declaration: section
origin: cited
lean: MathlibExt.Topology.HopfInvariantOneWanted.Topology.HopfInvariantOne.hSpace_sphere_iff, MathlibExt.Topology.Homotopy.BorsukUlamWanted.borsukUlam, MathlibExt.MeasureTheory.Geometry.HamSandwichWanted.ham_sandwich
statement: formalized
---

# Algebraic topology: its own results

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/index.html).

Homotopy groups, singular homology and other algebraic invariants of spaces, with classical theorems such as Borsuk–Ulam, Hurewicz and Hopf invariant one.

## Adams' theorem on spheres that are H-spaces

For every natural number $n$, the unit sphere
$S^n$ of the Euclidean space $\mathbb{R}^{n+1}$ admits an H-space structure if and only if
$n = 0$, $n = 1$, $n = 3$ or $n = 7$. Here an H-space structure on $S^n$ is a continuous map
$\mu \colon S^n \times S^n \to S^n$ together with a point $e \in S^n$ such that
$\mu(e, e) = e$ and the maps $x \mapsto \mu(e, x)$ and $x \mapsto \mu(x, e)$ are both homotopic
to the identity relative to $\{e\}$.

## Sources

- J. F. Adams, 'On the non-existence of elements of Hopf invariant one', Ann. of Math. 72 (1960), 20-104; J. F. Adams and M. F. Atiyah, 'K-theory and the Hopf invariant', Quart. J. Math. Oxford 17 (1966), 31-38. See also A. Hatcher, 'Algebraic Topology', Section 4.B. Problem `hSpace_sphere_iff` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.HopfInvariantOneWanted.Topology.HopfInvariantOne.hSpace_sphere_iff` is written with `theorem_wanted` in [WantedExt/Topology/HopfInvariantOneWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/HopfInvariantOneWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/index.html#h-space-sphere-iff).

## Borsuk–Ulam theorem

Let $n$ be a natural number and let $S^n$ be the unit sphere in the
Euclidean space $\mathbb{R}^{n+1}$. For every continuous map $f \colon S^n \to \mathbb{R}^n$ there
is a point $x \in S^n$ with $f(x) = f(-x)$.

## Sources

- K. Borsuk, Fund. Math. 20 (1933) 177–190 antipodal theorem; S. Ulam; J. Matoušek, Using the Borsuk–Ulam Theorem; Lean states `EuclideanSpace ℝ (Fin (n+1))` to `Fin n` specialization.

Formalized by `MathlibExt.Topology.Homotopy.BorsukUlamWanted.borsukUlam`, a theorem declared in [MathlibExt/Topology/Homotopy/BorsukUlam.lean, line 3676](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Homotopy/BorsukUlam.lean#L3676). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/index.html#borsuk-ulam).

## Ham sandwich theorem

Let $n \ge 1$ and let $\mu_1, \dots, \mu_n$ be finite Borel
measures on the Euclidean space $\mathbb{R}^n$, each absolutely continuous with respect to
Lebesgue measure. Then there exist a unit vector $v \in \mathbb{R}^n$ and a real number $t$
such that for every $i$, both closed half-spaces $\{x : \langle v, x \rangle \le t\}$ and
$\{x : \langle v, x \rangle \ge t\}$ have $\mu_i$-measure equal to $\mu_i(\mathbb{R}^n)/2$.

## Sources

- A. H. Stone and J. W. Tukey, Duke Math. J. 9 (1942) 356–359 ham sandwich theorem; J. Matoušek, Using the Borsuk–Ulam Theorem; Lean states measure-theoretic Euclidean specialization with `μ i ≪ volume` making the bisecting hyperplane null.

Formalized by `MathlibExt.MeasureTheory.Geometry.HamSandwichWanted.ham_sandwich`, a theorem declared in [MathlibExt/MeasureTheory/Geometry/HamSandwich.lean, line 414](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Geometry/HamSandwich.lean#L414). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/index.html#ham-sandwich).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Algebraic topology](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Topology/algebraic-topology)
