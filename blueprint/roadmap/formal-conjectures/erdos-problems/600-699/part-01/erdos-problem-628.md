---
declaration: theorem
origin: cited
lean: Erdos628.erdos_628, Erdos628.erdos_628.variants.k_5_a_3_b_3, Erdos628.erdos_628.variants.quasi_line, Erdos628.erdos_628.variants.independence_number_2
statement: formalized
---

# Erdős Problem 628

> *References:*
> - [erdosproblems.com/628](https://www.erdosproblems.com/628)
> - [BKPS09] Balogh, József and Kostochka, Alexandr V. and Prince, Noah and Stiebitz, Michael,
>   *The Erdős-Lovász Tihany conjecture for quasi-line graphs*. Discrete Math. (2009), 3985-3991.
> - [BrJu69] Brown, W. G. and Jung, H. A., *On odd circuits in chromatic graphs*. Acta Math. Acad.
>   Sci. Hungar. (1969), 129-134.
> - [Er68b] Erdős, P., *Problem 2*. Theory of Graphs (1968), 361.
> - [So22] Song, Zi-Xia, *A survey on the Erdős-Lovász Tihany conjecture*. Adv. Math. (China)
>   (2022), 259--274.

*Quoted from [FormalConjectures/ErdosProblems/628.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/628.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/628](https://www.erdosproblems.com/628).

The file states 4 research or textbook statements: 1 open and 3 solved.

## `Erdos628.erdos_628`

Open: stated without proof.

> Let $G$ be a graph with chromatic number $k$ containing no $K_k$. If $a,b\geq 2$ and $a+b=k+1$
> then must there exist two disjoint subgraphs of $G$ with chromatic numbers $\geq a$ and $\geq b$
> respectively?

```lean
theorem erdos_628 (V : Type*) [Fintype V] (G : SimpleGraph V) (k : ℕ)
    (hG_chrom : G.chromaticNumber = (k : ℕ∞))
    (hG_clique : G.CliqueFree k)
    (a b : ℕ) (ha : a ≥ 2) (hb : b ≥ 2) (hab : a + b = k + 1) :
    ∃ (s : Set V),
      (G.induce s).chromaticNumber ≥ (a : ℕ∞) ∧
      (G.induce sᶜ).chromaticNumber ≥ (b : ℕ∞)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/628.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/628.lean#L46).

## `Erdos628.erdos_628.variants.k_5_a_3_b_3`

Solved: stated here without proof.

> Erdős [Er68b] originally asked about $a=b=3$ which was proved by Brown and Jung [BrJu69] (who in fact prove that $G$ must contain two vertex disjoint odd cycles)..

```lean
theorem erdos_628.variants.k_5_a_3_b_3 (V : Type*) [Fintype V] (G : SimpleGraph V) [DecidableRel G.Adj]
    (hG_chrom : G.chromaticNumber = (5 : ℕ∞))
    (hG_clique : G.CliqueFree 5) :
    ∃ (s : Set V),
      (G.induce s).chromaticNumber ≥ (3 : ℕ∞) ∧
      (G.induce sᶜ).chromaticNumber ≥ (3 : ℕ∞)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/628.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/628.lean#L61).

## `Erdos628.erdos_628.variants.quasi_line`

Solved: stated here without proof.

> Balogh, Kostochka, Prince, and Stiebitz [BKPS09] proved the conjecture for quasi-line graphs.

```lean
theorem erdos_628.variants.quasi_line (V : Type*) [Fintype V] (G : SimpleGraph V) [DecidableRel G.Adj]
    (hG_quasi : IsQuasiLineGraph G)
    (k : ℕ)
    (hG_chrom : G.chromaticNumber = (k : ℕ∞))
    (hG_clique : G.CliqueFree k)
    (a b : ℕ) (ha : a ≥ 2) (hb : b ≥ 2) (hab : a + b = k + 1) :
    ∃ (s : Set V),
      (G.induce s).chromaticNumber ≥ (a : ℕ∞) ∧
      (G.induce sᶜ).chromaticNumber ≥ (b : ℕ∞)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/628.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/628.lean#L73).

## `Erdos628.erdos_628.variants.independence_number_2`

Solved: stated here without proof.

> Balogh, Kostochka, Prince, and Stiebitz [BKPS09] proved the conjecture for graphs with independence number 2.

```lean
theorem erdos_628.variants.independence_number_2 (V : Type*) [Fintype V] (G : SimpleGraph V) [DecidableRel G.Adj]
    (hG_indep : G.indepNum = 2)
    (k : ℕ)
    (hG_chrom : G.chromaticNumber = (k : ℕ∞))
    (hG_clique : G.CliqueFree k)
    (a b : ℕ) (ha : a ≥ 2) (hb : b ≥ 2) (hab : a + b = k + 1) :
    ∃ (s : Set V),
      (G.induce s).chromaticNumber ≥ (a : ℕ∞) ∧
      (G.induce sᶜ).chromaticNumber ≥ (b : ℕ∞)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/628.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/628.lean#L88).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/628.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/628.lean)
- [erdosproblems.com/628](https://www.erdosproblems.com/628)
