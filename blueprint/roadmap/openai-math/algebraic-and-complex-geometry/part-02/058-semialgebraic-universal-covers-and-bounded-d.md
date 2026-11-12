---
declaration: section
origin: cited
lean: OAI.Release061.main
statement: formalized
proof: formalized
---

# 058. Semialgebraic universal covers and bounded domains

2 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves the Kollár–Pardon conjecture: the semialgebraic universal covers of connected normal projective complex varieties are exactly products $D\times\mathbb C^m\times F$, with *D* bounded symmetric and *F* simply connected, normal, and projective. A universal cover is quasi-projective exactly when the bounded symmetric factor is absent. In particular, a smooth projective variety covered by ℂ$^{n}$ has a finite étale cover by an abelian variety.

## Semialgebraic universal covers of normal projective varieties

We prove the Kollár–Pardon conjecture: the universal cover of a connected normal projective complex variety is biholomorphic to a semialgebraic open subset of a projective variety if and only if it is a product of a bounded symmetric domain, a complex affine space, and a simply connected normal projective variety.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Semialgebraic-universal-covers-of-normal-projective-varieties-September-24-2026/paper.pdf).

## Symmetry of semialgebraic bounded domains with compact quotient

Every nonempty connected semialgebraic bounded open subset of a complex affine variety admitting a properly discontinuous cocompact group of biholomorphisms is smooth and biholomorphic to a bounded symmetric domain. This answers the bounded-domain question of Kollár and Pardon affirmatively.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Symmetry-of-semialgebraic-bounded-domains-with-compact-quotient-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result answers the paper's symmetry question affirmatively. A nonempty connected bounded semialgebraic subset, relatively open in a complex affine algebraic set, is smooth and biholomorphic to a bounded symmetric domain whenever a discrete group acts properly and holomorphically with compact quotient.

The action need not be free, and the ambient algebraic set may be singular.

## Lean: Symmetry of semialgebraic bounded domains

Stated in [SymmetricDomains.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SymmetricDomains.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main {n : ℕ} (V U : Set (Affine n))
    (hV : IsAffineAlgebraic V) (hUV : U ⊆ V)
    (hopen : IsOpen ((Subtype.val : V → Affine n) ⁻¹' U))
    (hconn : IsConnected U) (hsa : IsSemialgebraic U)
    (hbounded : Bornology.IsBounded U)
    (Γ : Type*) [Group Γ] [TopologicalSpace Γ] [DiscreteTopology Γ]
    [MulAction Γ U] [ProperSMul Γ U]
    [CompactSpace (Quotient (MulAction.orbitRel Γ U))]
    (hhol : ∀ γ : Γ, HolomorphicOnSubset U (fun p => (γ • p : U).val)) :
    IsSmooth U ∧ ∃ (m : ℕ) (D : Set (Affine m)),
      IsBoundedSymmetricDomain D ∧ Nonempty (Biholomorph U D)
```

Proved in [lean/OAI/Analysis/SymmetricDomains/Main.lean, line 55](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/SymmetricDomains/Main.lean#L55).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/058.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/058.md)
