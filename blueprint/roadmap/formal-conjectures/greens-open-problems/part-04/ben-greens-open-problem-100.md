---
declaration: theorem
origin: cited
lean: Green100.green_100.parts.i, Green100.green_100.parts.ii, Green100.green_100.variants.operator_norm, Green100.green_100.variants.sofic_isHyperlinear, Green100.green_100.variants.residuallyFinite_isSofic, Green100.green_100.variants.higman_isSofic, Green100.green_100.variants.higman_isHyperlinear, Green100.green_100.variants.helfgott_juschenko
statement: formalized
---

# Ben Green's Open Problem 100

> *References:*
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.100)
> - [Pe08] Pestov, V. G., *Hyperlinear and sofic groups: a brief guide*. Bull. Symbolic Logic 14
>   (2008), 449--480. [arXiv:0804.3968](https://arxiv.org/abs/0804.3968)
> - [HJ19] Helfgott, H. A. and Juschenko, K., *Soficity, short cycles, and the Higman group*.
>   Trans. Amer. Math. Soc. 371 (2019), 2771--2795.
>   [arXiv:1512.02135](https://arxiv.org/abs/1512.02135)
> - [Op26] OpenAI, *Non-sofic groups exist* (2026).
>   https://openai.com/index/ten-advances-in-mathematics/
> - [FF26] Fournier-Facio, F., *A torsion-free non-sofic group* (2026).
>   [arXiv:2608.02025](https://arxiv.org/abs/2608.02025)
> - [KT26] Kun, G. and Thom, A., *Nonsofic wreath products of residually finite groups* (2026).
>   [arXiv:2608.06222](https://arxiv.org/abs/2608.06222)
> - [Ec26] Eckhardt, C., *Non-MF groups and non-finite full group C\*-algebras* (2026).
>   [arXiv:2608.28772](https://arxiv.org/abs/2608.28772)
> - [Li26] Liu, J., *Nonhyperlinear groups exist* (2026).
>   https://jihaoliu.org/ai-results/nonhyperlinear-groups-exist-2026-09-20.pdf

*Quoted from [FormalConjectures/GreensOpenProblems/100.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/100.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 8 research or textbook statements: 2 open and 6 solved.

## `Green100.green_100.parts.i`

Solved: stated here without proof.

> Is every group well-approximated by finite groups? There are really two questions here, namely
> is every group sofic? and is every group hyperlinear? This is the first one: is every group sofic?
>
> We use the characterisation of soficity in [Pe08, Theorem 3.5], see `IsSofic`. It only involves
> finite subsets, so a group is sofic if all its finitely generated subgroups are. These are
> countable, so it is enough to quantify over groups in `Type`.
>
> [Gr24] lists this as open. The answer is no: OpenAI announced in 2026 that the unit group of the
> binary Leavitt algebra is not sofic [Op26], and Fournier-Facio [FF26, Theorem 1.3] gives a
> finitely presented torsion-free non-sofic group, using a criterion from [Op26]. Kun and Thom
> [KT26] give further non-sofic groups. These results are in 2026 preprints.

```lean
theorem green_100.parts.i : ¬ ∀ (G : Type) [Group G], IsSofic G
```

Category `research solved`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/GreensOpenProblems/100.lean, line 136](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/100.lean#L136).

## `Green100.green_100.parts.ii`

Solved: stated here without proof.

> Is every group well-approximated by finite groups? There are really two questions here, namely
> is every group sofic? and is every group hyperlinear? This is the second one: is every group
> hyperlinear?
>
> We use the characterisation of hyperlinearity in [Pe08, Theorem 3.6], see `IsHyperlinear`, with
> the normalised Hilbert–Schmidt norm. [Gr24] gives a precise form of this question with the
> operator norm instead, see `green_100.variants.operator_norm`. As for `green_100.parts.i`, it is
> enough to quantify over groups in `Type`.
>
> [Gr24] lists this as open. The answer is no: Liu [Li26, Theorem 1.1] constructs a countable group,
> a wreath product, that is not hyperlinear. This is a 2026 preprint.

```lean
theorem green_100.parts.ii : ¬ ∀ (G : Type) [Group G], IsHyperlinear G
```

Category `research solved`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md), [46 Functional analysis](../../by-subject/part-02/46-functional-analysis/README.md). Declared in [FormalConjectures/GreensOpenProblems/100.lean, line 153](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/100.lean#L153).

## `Green100.green_100.variants.operator_norm`

Solved: stated here without proof.

> Suppose that $G$ is a group. Is the following true? For every finite set $A \subset G$ containing
> the identity $e_G$ and for every $\varepsilon > 0$, there is some unitary group $U(n)$ and a map
> $\phi : A \to U(n)$ such that $\phi(e_G) = I_n$, such that $\phi$ is an 'approximate
> homomorphism' in the sense that $\|\phi(a_1 a_2) - \phi(a_1)\phi(a_2)\| < \varepsilon$ for all
> $a_1, a_2 \in A$ such that $a_1 a_2 \in A$, whilst $\phi$ is 'nontrivial' in the sense that
> $\|\phi(a) - I_n\| \ge 1$ for all $a \in A$, $a \ne e_G$. (Here $\|-\|$ is the
> $\ell^2$-to-$\ell^2$ operator norm.)
>
> [Gr24] gives this as a precise statement of `green_100.parts.ii`. In [Pe08], hyperlinearity uses
> the normalised Hilbert–Schmidt norm, and approximation in the operator norm defines a class of
> groups whose relation to hyperlinear groups was open there [Pe08, Remark 8.6 and Question 8.7];
> these are now usually called MF groups. We state the question as written, with the operator
> norm, for every group.
>
> [Gr24] lists this as open. The answer is no. Exhausting a countable group by finite sets
> containing the identity, with errors tending to zero, the maps $\phi$ give a homomorphism into the
> unitary group of $\prod_k M_{n_k}(\mathbb{C}) / \bigoplus_k M_{n_k}(\mathbb{C})$, which is
> injective by the bound $\|\phi(a) - I_n\| \ge 1$. So every countable group with this property is
> MF in the sense of [Ec26, Definition 4.1]. Eckhardt [Ec26, Theorem 4.3 and Examples 3.2 and 4.5]
> gives a countable group that is not MF, built from a property (T) group such as
> $\mathbb{Z}^3 \rtimes \mathrm{SL}_3(\mathbb{Z})$. This is a 2026 preprint.

```lean
theorem green_100.variants.operator_norm :
    ¬ ∀ (G : Type) [Group G], OperatorNormApprox G
```

Category `research solved`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md), [46 Functional analysis](../../by-subject/part-02/46-functional-analysis/README.md). Declared in [FormalConjectures/GreensOpenProblems/100.lean, line 180](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/100.lean#L180).

## `Green100.green_100.variants.sofic_isHyperlinear`

Solved: stated here without proof.

> Every sofic group is hyperlinear [Pe08, Theorem 3.3], a result of Elek and Szabó. The converse is
> not known [Gr24].

```lean
theorem green_100.variants.sofic_isHyperlinear (G : Type*) [Group G] (hG : IsSofic G) :
    IsHyperlinear G
```

Category `research solved`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md), [46 Functional analysis](../../by-subject/part-02/46-functional-analysis/README.md). Declared in [FormalConjectures/GreensOpenProblems/100.lean, line 189](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/100.lean#L189).

## `Green100.green_100.variants.residuallyFinite_isSofic`

Solved: stated here without proof.

> Every residually finite group is sofic [Pe08, Example 4.2].

```lean
theorem green_100.variants.residuallyFinite_isSofic (G : Type*) [Group G]
    [Group.ResiduallyFinite G] : IsSofic G
```

Category `research solved`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/GreensOpenProblems/100.lean, line 195](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/100.lean#L195).

## `Green100.green_100.variants.higman_isSofic`

Open: stated without proof.

> Is the Higman group sofic? [Gr24] notes that the Higman group is not known to be either
> hyperlinear or sofic.

```lean
theorem green_100.variants.higman_isSofic : IsSofic HigmanGroup
```

Category `research open`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/GreensOpenProblems/100.lean, line 204](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/100.lean#L204).

## `Green100.green_100.variants.higman_isHyperlinear`

Open: stated without proof.

> Is the Higman group hyperlinear? [Gr24] notes that the Higman group is not known to be either
> hyperlinear or sofic.

```lean
theorem green_100.variants.higman_isHyperlinear : IsHyperlinear HigmanGroup
```

Category `research open`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md), [46 Functional analysis](../../by-subject/part-02/46-functional-analysis/README.md). Declared in [FormalConjectures/GreensOpenProblems/100.lean, line 212](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/100.lean#L212).

## `Green100.green_100.variants.helfgott_juschenko`

Solved: stated here without proof.

> **Helfgott and Juschenko.** If the Higman group is sofic, then for every $\varepsilon > 0$ there
> is $N$ such that for every odd $n \ge N$ there is a bijection $f : \mathbb{Z}/n\mathbb{Z} \to
> \mathbb{Z}/n\mathbb{Z}$ with $f(x + 1) = 2 f(x)$ for at least $(1 - \varepsilon) n$ values of $x$
> and $f(f(f(f(x)))) = x$ for all $x$ [HJ19, Theorem 2, case $m = 2$]. The last condition already
> makes $f$ a bijection. [HJ19] presents the Higman group with the order of the generators
> reversed, which gives an isomorphic group.

```lean
theorem green_100.variants.helfgott_juschenko :
    IsSofic HigmanGroup → ∀ ε : ℝ, 0 < ε → ∃ N : ℕ, ∀ n : ℕ, N ≤ n → n.Coprime 2 →
      ∃ f : ZMod n → ZMod n, (1 - ε) * n ≤ Set.ncard {x | f (x + 1) = 2 * f x} ∧
        ∀ x, f (f (f (f x))) = x
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/GreensOpenProblems/100.lean, line 224](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/100.lean#L224).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/100.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/100.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.100)
