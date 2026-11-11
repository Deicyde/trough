---
declaration: theorem
origin: cited
lean: DifferentiableOn.eqOn_of_eqOn_re_gt
statement: formalized
proof: formalized
---

# Identity theorem on a right half-plane

Two functions holomorphic on `Re s > a` that
agree on some right half-plane `Re s > b` agree throughout `Re s > a`.

```lean
DifferentiableOn.eqOn_of_eqOn_re_gt.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℂ E]
  [CompleteSpace E] {f g : ℂ → E} {a b : ℝ} (hf : DifferentiableOn ℂ f {s | a < s.re})
  (hg : DifferentiableOn ℂ g {s | a < s.re}) (hfg : Set.EqOn f g {s | b < s.re}) :
  Set.EqOn f g {s | a < s.re}
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`DifferentiableOn.eqOn_of_eqOn_re_gt`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/HalfPlaneIdentity.html#DifferentiableOn.eqOn_of_eqOn_re_gt).

## Sources

- [Tau Ceti documentation: `DifferentiableOn.eqOn_of_eqOn_re_gt`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/HalfPlaneIdentity.html#DifferentiableOn.eqOn_of_eqOn_re_gt)
- [Source of `DifferentiableOn.eqOn_of_eqOn_re_gt` in TauCeti/Analysis/Complex/HalfPlaneIdentity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/HalfPlaneIdentity.lean#L23)
