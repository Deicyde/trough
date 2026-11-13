---
declaration: theorem
origin: cited
lean: Erdos910.erdos_910.parts.i, Erdos910.erdos_910.parts.ii, Erdos910.erdos_910.variants.rudin_CH
statement: formalized
---

# Erdős Problem 910

> *References:*
> - [erdosproblems.com/910](https://www.erdosproblems.com/910)
> - [Er82e] Erdős, Paul, *Some of my favourite problems which recently have been solved*. (1982),
>   59--79. [PDF](https://www.renyi.hu/~p_erdos/1982-33.pdf)
> - [Er44] Erdős, P., *Some remarks on connected sets*. Bull. Amer. Math. Soc. 50 (1944), 442-446.
>   [PDF](https://www.renyi.hu/~p_erdos/1944-06.pdf)
> - [Ru58] Rudin, M. E., *A connected subset of the plane*. Fund. Math. 46 (1958), 15-24.

*Quoted from [FormalConjectures/ErdosProblems/910.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/910.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/910](https://www.erdosproblems.com/910).

The file states 3 research or textbook statements: 2 open and 1 solved.

## `Erdos910.erdos_910.parts.i`

Open: stated without proof.

> Does every connected set in $\mathbb{R}^n$ contain a connected subset which is not a point and not
> homeomorphic to the original set?
>
> Asked by Erdős [Er44, p. 445], see also [Er82e, p. 77]. Following [Er44, pp. 443 and 445], a
> single point is not a connected set, so $X$ is required to have more than one point.
>
> Erdős [Er82e, p. 77] reports that Rudin, assuming the continuum hypothesis, found counterexamples
> to both questions of this problem. The theorem of [Ru58] (`erdos_910.variants.rudin_CH`) does not
> say that Rudin's set is homeomorphic to its connected subsets with more than one point. A
> counterexample that assumes the continuum hypothesis would not disprove this statement in ZFC.

```lean
theorem erdos_910.parts.i :
    ∀ (n : ℕ) (X : Set (EuclideanSpace ℝ (Fin n))), IsConnected X → X.Nontrivial →
      ∃ Y ⊆ X, IsConnected Y ∧ Y.Nontrivial ∧ ¬ Nonempty (Y ≃ₜ X)
```

Category `research open`; AMS [54 General topology](../../../by-subject/part-02/54-general-topology/README.md). Declared in [FormalConjectures/ErdosProblems/910.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/910.lean#L51).

## `Erdos910.erdos_910.parts.ii`

Open: stated without proof.

> If $n\geq 2$ does every connected set in $\mathbb{R}^n$ contain more than $2^{\aleph_0}$ many
> connected subsets?
>
> Erdős [Er82e, p. 77] asks this for connected sets of dimension greater than one; [Er44, p. 446]
> asks, for these sets, for $2^{\mathfrak{c}}$ connected subsets. The condition $n\geq 2$ alone
> would make the answer trivially no: a segment in $\mathbb{R}^2$ has only $2^{\aleph_0}$ connected
> subsets, its intervals. So we require `1 < smallInductiveDimension X`, which agrees with the
> covering dimension for subsets of $\mathbb{R}^n$. As in `erdos_910.parts.i`, single points are not
> counted as connected sets [Er44, p. 445].
>
> Rudin's set $M$ [Ru58] has at most $2^{\aleph_0}$ connected subsets, since each one with more than
> one point is $M$ minus a countable set. But $M$ lies in Rudin's continuum
> $I=\bigcap_n\Gamma_n^*$, where each $\Gamma_n$ is a chain of $2$-cells whose links have diameter
> less than $1/n$ [Ru58, 1.1-1.2], so $I$, and hence $M$, has dimension at most one. Rudin's set
> therefore does not answer this question as Erdős states it.

```lean
theorem erdos_910.parts.ii :
    ∀ (n : ℕ) (X : Set (EuclideanSpace ℝ (Fin n))), IsConnected X →
      1 < smallInductiveDimension X →
      𝔠 < Cardinal.mk {Y : Set (EuclideanSpace ℝ (Fin n)) |
        Y ⊆ X ∧ IsConnected Y ∧ Y.Nontrivial}
```

Category `research open`; AMS [54 General topology](../../../by-subject/part-02/54-general-topology/README.md). Declared in [FormalConjectures/ErdosProblems/910.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/910.lean#L74).

## `Erdos910.erdos_910.variants.rudin_CH`

Solved: stated here without proof.

> Assume the continuum hypothesis. Rudin [Ru58, p. 15] constructed a connected subset $M$ of the
> plane, with more than one point, such that $M\setminus N$ is at most countable for every connected
> subset $N\subseteq M$ with more than one point.
>
> This disproves a conjecture of Erdős [Er44, p. 443] that every connected set $C$ contains a
> connected subset $C'$ such that $C\setminus C'$ has cardinality $2^{\aleph_0}$. Erdős [Er82e,
> p. 77] reports that Rudin's examples answer both questions of this problem in the negative; see
> the docstrings of `erdos_910.parts.i` and `erdos_910.parts.ii`.

```lean
theorem erdos_910.variants.rudin_CH :
    (ℵ₁ = 𝔠) → ∃ M : Set (EuclideanSpace ℝ (Fin 2)), IsConnected M ∧ M.Nontrivial ∧
      ∀ N ⊆ M, IsConnected N → N.Nontrivial → (M \ N).Countable
```

Category `research solved`; AMS [54 General topology](../../../by-subject/part-02/54-general-topology/README.md). Declared in [FormalConjectures/ErdosProblems/910.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/910.lean#L92).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/910.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/910.lean)
- [erdosproblems.com/910](https://www.erdosproblems.com/910)
