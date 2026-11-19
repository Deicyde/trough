---
declaration: def
origin: cited
lean: TauCeti.Perfectoid.uniformTilt
statement: formalized
---

# TauCeti.Perfectoid.uniformTilt

The *tilt* `B♭ = lim_{x ↦ x ^ p} B` of a complete uniform Tate ring `B` in which `p` is
topologically nilpotent: Mathlib's monoid `Perfection B p` of compatible systems of `p`-th roots,
renamed to carry the ring structure with the limit addition (`uniformTilt.instCommRing`).

```lean
TauCeti.Perfectoid.uniformTilt.{u_1} (p : ℕ) (B : Type u_1) [CommRing B] : Type u_1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Perfectoid.uniformTilt`](https://taucetiproject.org/docs/TauCeti/RingTheory/Perfectoid/UniformTilt/Basic.html#TauCeti.Perfectoid.uniformTilt).

## Sources

- [Tau Ceti documentation: `TauCeti.Perfectoid.uniformTilt`](https://taucetiproject.org/docs/TauCeti/RingTheory/Perfectoid/UniformTilt/Basic.html#TauCeti.Perfectoid.uniformTilt)
- [Source of `TauCeti.Perfectoid.uniformTilt` in TauCeti/RingTheory/Perfectoid/UniformTilt/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Perfectoid/UniformTilt/Basic.lean#L113)
- [Tau Ceti roadmap status: Perfectoid rings and spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PerfectoidSpaces/STATUS.md)
