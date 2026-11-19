---
declaration: theorem
origin: cited
lean: OnePoint.eq_zero_of_mdifferentiable_section_twistCore
statement: formalized
proof: formalized
---

# Vanishing theorem: `H⁰(𝒪(k)) = 0` for `k < 0`

On the Riemann sphere, every holomorphic
section of `𝒪(k)` with `k < 0` vanishes identically.

```lean
OnePoint.eq_zero_of_mdifferentiable_section_twistCore {k : ℤ} (hk : k < 0) {s : OnePoint ℂ → ℂ}
  (hs : MDiff fun x => ⟨x, s x⟩) : s = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`OnePoint.eq_zero_of_mdifferentiable_section_twistCore`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Instances/OnePoint/LineBundle/Sections.html#OnePoint.eq_zero_of_mdifferentiable_section_twistCore).

## Sources

- [Tau Ceti documentation: `OnePoint.eq_zero_of_mdifferentiable_section_twistCore`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Instances/OnePoint/LineBundle/Sections.html#OnePoint.eq_zero_of_mdifferentiable_section_twistCore)
- [Source of `OnePoint.eq_zero_of_mdifferentiable_section_twistCore` in TauCeti/Geometry/Manifold/Instances/OnePoint/LineBundle/Sections.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Instances/OnePoint/LineBundle/Sections.lean#L291)
