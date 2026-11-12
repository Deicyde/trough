---
declaration: section
origin: cited
lean: OAI.Problem047.koebe_circle_domain, OAI.Problem047.removability_implies_rigidity
statement: formalized
proof: formalized
---

# 071. Koebe’s circle-domain conjecture

2 manuscripts and 4 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves the existence part of Koebe's circle-domain conjecture: every domain in the Riemann sphere is conformally equivalent to a domain whose complementary components are round disks or points. It also proves that circle domains with conformally removable boundary are rigid, meaning every conformal equivalence to another circle domain is Möbius, establishing this direction of the He–Schramm conjecture.

## Removable Boundaries and Rigidity of Circle Domains

We prove that a circle domain with conformally removable boundary is conformally rigid, with no restriction on the number of complementary components. This establishes the removability-to-rigidity direction of the He–Schramm Conjecture.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Removable-Boundaries-and-Rigidity-of-Circle-Domains-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## Koebe's Circle-Domain Conjecture

We prove that every domain in the Riemann sphere is conformally equivalent to a circle domain, resolving Koebe's circle-domain conjecture positively.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Koebes-Circle-Domain-Conjecture-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves the removability-to-rigidity direction of the He–Schramm conjecture. If a circle domain has conformally removable boundary, then every conformal equivalence from it to another circle domain agrees on the source with a Möbius transformation. There is no bound on the number of complementary components.

The same Comparator file also states Koebe's circle-domain theorem, which gives a circle-domain representative for every domain in the Riemann sphere.

Koebe's circle-domain conjecture asks whether every domain in the Riemann sphere is conformally equivalent to a circle domain, whose complementary components are round disks or points. The formalization proves this for every domain. It also proves rigidity under a separate hypothesis: a conformal equivalence between circle domains is a Möbius transformation when the source boundary is conformally removable.

## Lean: Removable-boundary rigidity and the circle-domain theorem

Stated in [KoebeCircleDomains.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/KoebeCircleDomains.lean).

```lean
theorem koebe_circle_domain :
    ∀ U : Set Sphere, IsOpen U → IsConnected U →
      ∃ (V : Set Sphere) (f : Sphere → Sphere),
        IsCircleDomain V ∧ IsConformalEquivalence f U V
```

Proved in [lean/OAI/Analysis/CircleDomains/Main.lean, line 10](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/CircleDomains/Main.lean#L10).

```lean
theorem removability_implies_rigidity :
    ∀ (U V : Set Sphere) (f : Sphere → Sphere),
      IsCircleDomain U → IsCircleDomain V →
      IsConformallyRemovable (frontier U) → IsConformalEquivalence f U V →
      ∃ M : Mobius, ∀ p ∈ U, f p = M • p
```

Proved in [lean/OAI/Analysis/CircleDomains/Main.lean, line 16](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/CircleDomains/Main.lean#L16).

## Lean: Koebe's circle-domain theorem and removable-boundary rigidity

Stated in [KoebeCircleDomains.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/KoebeCircleDomains.lean).

```lean
theorem koebe_circle_domain :
    ∀ U : Set Sphere, IsOpen U → IsConnected U →
      ∃ (V : Set Sphere) (f : Sphere → Sphere),
        IsCircleDomain V ∧ IsConformalEquivalence f U V
```

Proved in [lean/OAI/Analysis/CircleDomains/Main.lean, line 10](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/CircleDomains/Main.lean#L10).

```lean
theorem removability_implies_rigidity :
    ∀ (U V : Set Sphere) (f : Sphere → Sphere),
      IsCircleDomain U → IsCircleDomain V →
      IsConformallyRemovable (frontier U) → IsConformalEquivalence f U V →
      ∃ M : Mobius, ∀ p ∈ U, f p = M • p
```

Proved in [lean/OAI/Analysis/CircleDomains/Main.lean, line 16](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/CircleDomains/Main.lean#L16).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/071.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/071.md)
