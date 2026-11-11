---
declaration: theorem
origin: cited
lean: ContIntertwiningMap.coind₁_ext
statement: formalized
proof: formalized
---

# Frobenius reciprocity for `coind₁`, uniqueness

Two intertwining maps into a coinduced
representation that agree after evaluation at `1` are equal.

```lean
ContIntertwiningMap.coind₁_ext.{u_1, u_2, u_3, u_4} {R : Type u_1} {G : Type u_2} {V : Type u_3}
  {W : Type u_4} [Ring R] [TopologicalSpace R] [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
  [AddCommGroup V] [_root_.Module R V] [TopologicalSpace V] [IsTopologicalAddGroup V]
  [AddCommGroup W] [_root_.Module R W] [TopologicalSpace W] [IsTopologicalAddGroup W]
  [ContinuousSMul R W] {π : ContRepresentation R G V} {σ : ContRepresentation R G W}
  {f g : ContIntertwiningMap π σ.coind₁} (h : ∀ (v : V), (f v) 1 = (g v) 1) : f = g
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContIntertwiningMap.coind₁_ext`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Continuous/Coinduced.html#ContIntertwiningMap.coind%E2%82%81_ext).

## Sources

- [Tau Ceti documentation: `ContIntertwiningMap.coind₁_ext`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Continuous/Coinduced.html#ContIntertwiningMap.coind%E2%82%81_ext)
- [Source of `ContIntertwiningMap.coind₁_ext` in TauCeti/RepresentationTheory/Continuous/Coinduced.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Continuous/Coinduced.lean#L128)
