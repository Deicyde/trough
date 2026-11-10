---
declaration: theorem
origin: cited
lean: Erdos597.erdos_597, Erdos597.erdos_597.variants.finite, Erdos597.erdos_597.variants.erdos_hajnal, Erdos597.erdos_597.variants.baumgartner
statement: formalized
---

# Erdős Problem 597

> *Reference:* [erdosproblems.com/597](https://www.erdosproblems.com/597)
>
> *References:*
> - [Er87] Erdős, P., *Some problems on finite and infinite graphs*. Logic and combinatorics
>   (Arcata, Calif., 1985) (1987), 223-228.

*Quoted from [FormalConjectures/ErdosProblems/597.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/597.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/597](https://www.erdosproblems.com/597).

The file states 4 research or textbook statements: 2 open and 2 solved. It also has 1 test statement, counted here but not shown.

## `Erdos597.erdos_597`

Open: stated without proof.

> **Erdős Problem 597** [Er87]. Let $G$ be a graph on at most $\aleph_1$
> vertices which contains no $K_4$ and no $K_{\aleph_0,\aleph_0}$ (the complete bipartite
> graph with $\aleph_0$ vertices in each class). Is it true that
>
> $$\omega_1^2 \to (\omega_1 \omega, G)^2?$$

```lean
theorem erdos_597 :
    ∀ (W : Type) (G : SimpleGraph W), #W ≤ ℵ_ 1 → G.CliqueFree 4 →
      (¬ ∃ A B : Set W, Disjoint A B ∧ A.Infinite ∧ B.Infinite ∧
        ∀ a ∈ A, ∀ b ∈ B, G.Adj a b) →
      OrdinalGraphRamsey ((ω_ 1) ^ (2 : ℕ)) ((ω_ 1) * ω) G
```

Category `research open`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/597.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/597.lean#L63).

## `Erdos597.erdos_597.variants.finite`

Open: stated without proof.

> **Erdős Problem 597, finite case** [Er87]. Is it true that
> $\omega_1^2 \to (\omega_1 \omega, G)^2$ for every finite $K_4$-free graph $G$?
> (A finite graph contains no $K_{\aleph_0,\aleph_0}$, so that hypothesis is vacuous.)

```lean
theorem erdos_597.variants.finite :
    ∀ (W : Type) [Fintype W] (G : SimpleGraph W), G.CliqueFree 4 →
      OrdinalGraphRamsey ((ω_ 1) ^ (2 : ℕ)) ((ω_ 1) * ω) G
```

Category `research open`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/597.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/597.lean#L76).

## `Erdos597.erdos_597.variants.erdos_hajnal`

Solved: stated here without proof.

> Erdős and Hajnal proved that $\omega_1^2 \to (\omega_1 \omega, 3)^2$: in every red/blue
> colouring of the edges of the complete graph on $\omega_1^2$ there is either a red clique
> of order type $\omega_1 \cdot \omega$ or a blue triangle.

```lean
theorem erdos_597.variants.erdos_hajnal :
    OrdinalCardinalRamsey ((ω_ 1) ^ (2 : ℕ)) ((ω_ 1) * ω) 3
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/597.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/597.lean#L87).

## `Erdos597.erdos_597.variants.baumgartner`

Solved: stated here without proof.

> Erdős originally asked Problem 597 with just the assumption that $G$ is $K_4$-free, but
> Baumgartner proved that $\omega_1^2 \not\to (\omega_1 \omega, K_{\aleph_0,\aleph_0})^2$.

```lean
theorem erdos_597.variants.baumgartner :
    ¬ OrdinalGraphRamsey ((ω_ 1) ^ (2 : ℕ)) ((ω_ 1) * ω) (completeBipartiteGraph ℕ ℕ)
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/597.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/597.lean#L96).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/597.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/597.lean)
- [erdosproblems.com/597](https://www.erdosproblems.com/597)
