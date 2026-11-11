---
declaration: theorem
origin: cited
lean: Representation.IntertwiningMap.exists_leftInverse_of_injective
statement: formalized
proof: formalized
---

# Maschke's theorem for intertwining maps

Over a field in which the order of the finite
group `G` is invertible, an injective intertwining map `f : ρ → σ` has an intertwining left
inverse `p : σ → ρ`, that is, `p ∘ f = id`.

```lean
Representation.IntertwiningMap.exists_leftInverse_of_injective.{u_1, u_2, u_3, u_4} {k : Type u_1}
  {G : Type u_2} {V : Type u_3} {W : Type u_4} [Field k] [Group G] [Finite G] [NeZero ↑(Nat.card G)]
  [AddCommGroup V] [_root_.Module k V] [AddCommGroup W] [_root_.Module k W]
  {ρ : Representation k G V} {σ : Representation k G W} (f : ρ.IntertwiningMap σ)
  (hf : Function.Injective ⇑f) : ∃ p, p.comp f = Representation.IntertwiningMap.id ρ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Representation.IntertwiningMap.exists_leftInverse_of_injective`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Maschke.html#Representation.IntertwiningMap.exists_leftInverse_of_injective).

## Sources

- [Tau Ceti documentation: `Representation.IntertwiningMap.exists_leftInverse_of_injective`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Maschke.html#Representation.IntertwiningMap.exists_leftInverse_of_injective)
- [Source of `Representation.IntertwiningMap.exists_leftInverse_of_injective` in TauCeti/RepresentationTheory/Maschke.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Maschke.lean#L55)
