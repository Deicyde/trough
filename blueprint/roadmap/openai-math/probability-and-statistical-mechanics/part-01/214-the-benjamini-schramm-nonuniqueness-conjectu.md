---
declaration: section
origin: cited
lean: OAI.Percolation.BenjaminiSchramm.full_main, OAI.Percolation.BenjaminiSchramm.critical_laws, OAI.Percolation.arbitrary_cayley
statement: formalized
---

# 214. The Benjamini–Schramm nonuniqueness conjecture

1 manuscript and 4 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves $p_c\lt p_u$ for Bernoulli bond percolation on every infinite connected locally finite nonamenable quasi-transitive graph, resolving the Benjamini–Schramm nonuniqueness conjecture. Thus there is a nonempty range of probabilities with infinitely many infinite clusters. A stronger operator bound also establishes the critical triangle condition.

## Nonuniqueness of percolation on nonamenable quasi-transitive graphs

We prove the bond-percolation nonuniqueness conjecture of Benjamini and Schramm: every infinite connected, locally finite, nonamenable quasi-transitive graph has a nonempty interval of parameters for which Bernoulli bond percolation almost surely has infinitely many infinite clusters. We also prove Hutchcroft's stronger operator-threshold conjecture, establishing $p_c\lt p_{2\to2}\le p_u$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves the nonuniqueness phase conjecture for Bernoulli bond percolation on infinite connected locally finite nonamenable quasi-transitive graphs. It establishes $p_c<p_{2\to2}\le p_u$ and a common nonempty coupled interval with infinitely many infinite clusters almost surely. For Cayley graphs, the result holds for every finite symmetric generating set of a nonamenable finitely generated group and every $p\in(p_c,p_u)$.

The selected critical estimates include a finite triangle diagram, susceptibility of order $(p_c-p)^{-1}$, percolation probability of order $p-p_c$, cluster-volume tail of order $n^{-1/2}$, and intrinsic and extrinsic radius tails of order $n^{-1}$. Connection probabilities decay exponentially below $p_{2\to2}$.

## Lean: Nonuniqueness phase and critical laws on quasi-transitive graphs

Stated in [BenjaminiSchramm.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BenjaminiSchramm.lean).

```lean
theorem full_main {V : Type u} {E : Type v} [Infinite V]
    (G : BondGraph V E) (hc : Connected G) (hl : LocallyFinite G)
    (hq : QuasiTransitive G) (hh : 0 < hV G) : MainConclusion G
```

Proved in [lean/OAI/Probability/BenjaminiSchramm/Main.lean, line 9](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/BenjaminiSchramm/Main.lean#L9).

```lean
theorem cayley_main {Λ : Type u} [Group Λ]
    (S : Finset Λ) (hsym : ∀ s ∈ S, s⁻¹ ∈ S) (_hone : 1 ∉ S)
    (hgen : Subgroup.closure (S : Set Λ) = ⊤) (hna : ¬ FolnerAmenable Λ) :
    OperatorBounded (cayleyBond S) (pc (cayleyBond S)) ∧
      MainConclusion (cayleyBond S) ∧
      ∀ p : unitInterval, pc (cayleyBond S) < p → p < pu (cayleyBond S) →
        ∀ᵐ ω ∂law p, (infiniteClusters (cayleyBond S) ω).Infinite
```

Its proof is in [lean/OAI/Probability/BenjaminiSchramm/Main.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/BenjaminiSchramm/Main.lean) or a file it imports further down, which this chapter does not read.

```lean
theorem critical_laws {V : Type u} {E : Type v} [Infinite V]
    (G : BondGraph V E) (hc : Connected G) (hl : LocallyFinite G)
    (hq : QuasiTransitive G) (hh : 0 < hV G) : CriticalLawsConclusion G
```

Proved in [lean/OAI/Probability/BenjaminiSchramm/Main.lean, line 14](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/BenjaminiSchramm/Main.lean#L14).

## Lean: Nonuniqueness for every nonamenable Cayley graph

Stated in [CayleyPercolation.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CayleyPercolation.lean).

```lean
theorem arbitrary_cayley {Λ : Type u} [Group Λ] [Group.FG Λ]
    (hna : ¬ AmenableGroup Λ) (S : Finset Λ)
    (hsym : ∀ s ∈ S, s⁻¹ ∈ S) (hgen : Subgroup.closure (S : Set Λ) = ⊤)
    (h1 : 1 ∉ S) :
    OperatorBounded (cayleyGraph S) (pc (cayleyGraph S)) ∧
    pc (cayleyGraph S) < ptwo (cayleyGraph S) ∧
    ptwo (cayleyGraph S) ≤ pu (cayleyGraph S) ∧
    (∃ p₁ p₂ : unitInterval, pc (cayleyGraph S) < p₁ ∧ p₁ < p₂ ∧ p₂ < 1 ∧
      ∀ᵐ labels ∂(labelLaw : Measure (CayleyEdge S → unitInterval)),
        ∀ p ∈ Set.Icc p₁ p₂, (infiniteClusters (cayleyGraph S) (openEdges labels p)).Infinite) ∧
    (∀ p : unitInterval, pc (cayleyGraph S) < p → p < pu (cayleyGraph S) →
      ∀ᵐ ω ∂law p, (infiniteClusters (cayleyGraph S) ω).Infinite)
```

Proved in [lean/OAI/Probability/UnimodularPercolation/Cayley/Nonuniqueness.lean, line 18](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/UnimodularPercolation/Cayley/Nonuniqueness.lean#L18).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/214.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/214.md)
