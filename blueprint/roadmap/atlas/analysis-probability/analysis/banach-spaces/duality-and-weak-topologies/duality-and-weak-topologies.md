---
declaration: section
origin: cited
lean: MetaMathlibExt.goldstine, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook10Wanted.continuousLinearFunctionalFiniteEvaluations, MathlibExt.Analysis.FunctionalAnalysis.BanachSpaceWanted.eberlein_smulian, MathlibExt.Analysis.FunctionalAnalysis.DunfordPettisWanted.dunford_pettis_compactness, MathlibExt.Analysis.FunctionalAnalysis.BanachLimit.banach_limit, MathlibExt.Analysis.FunctionalAnalysis.JosefsonNissenzweigWanted.josefson_nissenzweig, MathlibExt.Analysis.FunctionalAnalysis.BanachSpaceWanted.krein_smulian, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook24Wanted.additiveFunctionalMeasurableOnCurvesContinuous
statement: formalized
---

# Duality, weak topologies and reflexivity: its own results

10 results, 7 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/index.html).

Hahn–Banach, annihilators and bipolars, weak and weak-star convergence and topologies, Goldstine, James, Eberlein–Šmulian, Krein–Šmulian, Banach–Alaoglu, Mazur's lemma, Banach limits, Hamel bases and discontinuous functionals, F-spaces and locally convex spaces, Choquet theory.

## Goldstine's theorem

Let $E$ be a normed space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$,
let $E^{**}$ be its bidual and let $J : E \to E^{**}$ be the canonical embedding. In the
weak-star topology of $E^{**}$, the closure of the image under $J$ of the closed unit ball of $E$
is exactly the closed unit ball of $E^{**}$.

## Sources

- H. H. Goldstine, Weakly complete Banach spaces, Duke Math. J. 4 (1938), DOI 10.1215/S0012-7094-38-00410-7; Rudin, Functional Analysis, 2nd ed.; Lean states `RCLike` field case with metric closedBall formulation.

Formalized by `MetaMathlibExt.goldstine`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/BanachSpace.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/BanachSpace.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/index.html#goldstine).

## Continuous linear functionals on the space of all real functions

Let $H$ be a set and give
the space $\mathbb{R}^H$ of all real-valued functions on $H$ the topology of pointwise
convergence. Then for every continuous linear functional $f \colon \mathbb{R}^H \to \mathbb{R}$
there are a natural number $n$, points $t_1, \dots, t_n \in H$ and real numbers
$\alpha_1, \dots, \alpha_n$ such that $f(x) = \sum_{i=1}^n \alpha_i \, x(t_i)$ for every
$x \in \mathbb{R}^H$.

Continuity is the intended reading of the typescript, whose statement prints no continuity
hypothesis. Without continuity the claim is false: when $H$ is infinite, the algebraic dual of
$\mathbb{R}^H$ is strictly larger than the span of the evaluations.

## Sources

- S. Banach and S. Mazur, Problem 10 of the Scottish Book, stated as a theorem in the Scottish Book typescript.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook10Wanted.continuousLinearFunctionalFiniteEvaluations` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook10Wanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/ScottishBook10Wanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/index.html#continuous-linear-functional-finite-eval).

## Eberlein–Šmulian theorem

Let $E$ be a Banach space over $\mathbb{K} = \mathbb{R}$ or
$\mathbb{C}$. A subset of $E$ is compact in the weak topology if and only if it is sequentially
compact in the weak topology, that is, every sequence in it has a subsequence that converges
weakly to a point of the subset.

## Sources

- W. F. Eberlein, Weak Compactness in Banach Spaces, PNAS 33 (1947), 51–53, DOI 10.1073/pnas.33.3.51, and V. Smulian (1947); Dunford-Schwartz, Linear Operators I, 1958, V.5-6; Lean states `RCLike` Banach case with `IsCompact ↔ IsSeqCompact` in `WeakSpace`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.BanachSpaceWanted.eberlein_smulian`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/EberleinSmulian.lean, line 807](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/EberleinSmulian.lean#L807). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/index.html#eberlein-smulian).

## Dunford–Pettis weak compactness criterion

Let $\mu$ be a finite measure on a measurable
space $\alpha$ and let $(f_i)_{i \in \iota}$ be a family of integrable real functions on $\alpha$.
The family is uniformly integrable, meaning that it is bounded in $L^1(\mu)$ and that for every
$\varepsilon > 0$ there is $\delta > 0$ with $\int_s |f_i| \, d\mu \le \varepsilon$ for every $i$
and every measurable set $s$ with $\mu(s) \le \delta$, if and only if the closure of the set of
classes $\{[f_i] : i \in \iota\}$ in the weak topology of $L^1(\mu)$ is weakly compact.

## Sources

- N. Dunford and B. J. Pettis, Linear Operations on Summable Functions, Trans. Amer. Math. Soc. 47 (1940), 323–392, DOI 10.1090/S0002-9947-1940-0002020-4, criterion for weak compactness in `L¹`; Dunford-Schwartz IV; Lean states finite-measure real `L¹` specialization with weak-space closure characterization.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.DunfordPettisWanted.dunford_pettis_compactness`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/DunfordPettis.lean, line 1234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/DunfordPettis.lean#L1234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/index.html#dunford-pettis-compactness).

## Existence of Banach limits

There is a continuous linear functional $L$ on the real Banach
space $\ell^\infty$ of bounded real sequences with the supremum norm such that $L(f) \ge 0$
whenever $f_n \ge 0$ for every $n$, $L$ maps the constant sequence $1$ to $1$, $L(f) = L(g)$
whenever $g_n = f_{n+1}$ for every $n$, and $L(f) = l$ whenever the sequence $f_n$ converges
to $l$.

## Sources

- S. Banach, Theorie des operations lineaires, 1932, definition of generalised limit; G. Lorentz, Acta Math. 80 (1948) 167-190; Lean formalizes ℓ∞ via `BoundedContinuousFunction ℕ ℝ` and real field `ℝ` with all four classical axioms.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.BanachLimit.banach_limit`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/BanachLimit.lean, line 401](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/BanachLimit.lean#L401). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/index.html#banach-limit).

## Josefson–Nissenzweig theorem

Let $E$ be an infinite-dimensional Banach space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$. Then there is a sequence $(\varphi_n)_{n \in \mathbb{N}}$
of continuous linear functionals on $E$ with $\|\varphi_n\| = 1$ for every $n$ such that
$\varphi_n(x) \to 0$ for every $x \in E$; that is, the unit sphere of the dual of $E$ contains a
weak-star null sequence.

Proof: We apply Rosenthal's `ℓ¹` dichotomy to a separated dual sequence, then use the stable-block
and Banach-limit/Rademacher route of Hagler--Johnson (1977) and Behrends (1995).

## Sources

- B. Josefson, Weak sequential convergence in the dual of a Banach space does not imply norm convergence, Bull. Amer. Math. Soc. 81 (1975), 166–168, DOI 10.1090/S0002-9904-1975-13691-3; and A. Nissenzweig, w* sequential convergence, Israel J. Math. 22 (1975), 266–272, DOI 10.1007/BF02761594, Josefson-Nissenzweig theorem; Diestel, Sequences and Series; Lean states `RCLike` infinite-dimensional Banach case with `‖φ n‖=1` and pointwise weak-star nullness.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.JosefsonNissenzweigWanted.josefson_nissenzweig`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/JosefsonNissenzweig.lean, line 1707](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/JosefsonNissenzweig.lean#L1707). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/index.html#josefson-nissenzweig).

## Krein–Smulian theorem

Let $E$ be a Banach space over $\mathbb{K} = \mathbb{R}$ or
$\mathbb{C}$, and let $C$ be a subset of its dual $E^*$ that is convex over $\mathbb{R}$. Then $C$
is weak-star closed if and only if, for every $r > 0$, the set
$\{\varphi \in C : \|\varphi\| \le r\}$ is weak-star closed.

## Sources

- M. Krein and V. Smulian, Ann. of Math. 41 (1940) 556-583; Dunford-Schwartz I; Lean states `RCLike` Banach case with `Convex ℝ s` and closedBall intersections.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.BanachSpaceWanted.krein_smulian`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/KreinSmulian.lean, line 800](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/KreinSmulian.lean#L800). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/index.html#krein-smulian).

## Mazur's Problem 24: additive functionals measurable along curves are continuous

Let $E$
be a real Banach space and let $F \colon E \to \mathbb{R}$ be additive, that is,
$F(x + y) = F(x) + F(y)$ for all $x, y \in E$. If for every continuous map
$x \colon [0, 1] \to E$ the function $t \mapsto F(x(t))$ on $[0, 1]$ is Borel measurable,
then $F$ is continuous.

## Sources

- S. Mazur, Problem 24 of the Scottish Book (prize: two small beers). Solved affirmatively by I. Labuda and R. D. Mauldin, "Problem 24 of the Scottish Book concerning additive functionals", Colloquium Mathematicum 48, as quoted in Ger (2016); the proof covers additive operators into a Hausdorff topological vector space.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook24Wanted.additiveFunctionalMeasurableOnCurvesContinuous` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook24Wanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/ScottishBook24Wanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/index.html#additive-functional-measurable-on-curves).

## Nearest points in reflexive Banach spaces

Let $X$ be a reflexive complex Banach space, that
is, the canonical embedding of $X$ into its double dual is surjective, and let $C \subseteq X$ be a
nonempty closed convex set. Then for every $x_0 \in X$ there is $y_0 \in C$ such that
$\|x_0 - y_0\| = \inf_{y \in C} \|x_0 - y\|$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functional analysis; Normed linear spaces and Banach spaces; Banach lattices), problem `ma_proofbench_l2_64`.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ReflexiveBanachNearestPointWanted.exists_norm_sub_eq_iInf_of_reflexive_of_convex_of_isClosed` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ReflexiveBanachNearestPointWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/ReflexiveBanachNearestPointWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/index.html#exists-norm-sub-eq-i-inf-of-reflexive-of).

## Principle of local reflexivity

Let $E$ be a Banach space over $\mathbb{K} = \mathbb{R}$ or
$\mathbb{C}$, with dual $E^*$, bidual $E^{**}$ and canonical embedding $J \colon E \to E^{**}$.
Let $M$ and $N$ be finite-dimensional normed spaces over $\mathbb{K}$ with injective bounded
linear maps $i_M \colon M \to E^{**}$ and $i_N \colon N \to E^*$, and let $\varepsilon > 0$. Then
there is a bounded linear map $T \colon M \to E$ such that for all $m \in M$, $n \in N$ and
$x \in E$ we have
$(1 + \varepsilon)^{-1} \|i_M(m)\| \le \|T m\| \le (1 + \varepsilon) \|i_M(m)\|$,
$i_N(n)(T m) = i_M(m)(i_N(n))$, and $T m = x$ whenever $i_M(m) = J x$.

Proof: Helly's lemma applied to finitely many linear conditions plus one norm bound, then a finite
$\delta$-net of the unit sphere of $i_M(M)$ turns net-point bounds into the $(1+\varepsilon)$
bounds (the elementary proof in Albiac–Kalton, *Topics in Banach Space Theory*).

## Sources

- J. Lindenstrauss and H. Rosenthal, Israel J. Math. 7 (1969) 325-349, principle of local reflexivity; Johnson-Rosenthal-Zippin 1971 refinements; Albiac and Kalton, Topics in Banach Space Theory; Lean states `RCLike` Banach finite- dimensional `M, N` version with `(1+ε)`-isometry and pairing preservation.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.LocalReflexivityWanted.principle_of_local_reflexivity`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/LocalReflexivity.lean, line 1591](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/LocalReflexivity.lean#L1591). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/index.html#principle-of-local-reflexivity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Duality, weak topologies and reflexivity](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/banach-spaces/duality-and-weak-topologies)
