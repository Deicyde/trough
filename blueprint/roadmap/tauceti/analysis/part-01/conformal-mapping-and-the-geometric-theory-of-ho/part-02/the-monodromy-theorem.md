---
declaration: theorem
origin: cited
lean: TauCeti.monodromy_theorem, TauCeti.continuesInside_iff_exists_analyticOnNhd
statement: formalized
proof: formalized
---

# The monodromy theorem

Let `h` be a homotopy rel endpoints between two paths from `z₀` to
`z₁` in `ℂ`, and suppose a germ at `z₀` continues along every path `h (t, ·)` of the homotopy,
all the continuations starting from that one germ. Then they all end at one and the same germ at
`z₁`: the result of the continuation depends on the path only through its homotopy class.

This is the rel-endpoints case of `TauCeti.monodromy_theorem_of_free_homotopy`, whose homotopy is
allowed to move the endpoints and whose conclusion is correspondingly a continuation along the
path the terminal point sweeps out rather than a single germ at `z₁`.

```lean
TauCeti.monodromy_theorem.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℂ E]
  [CompleteSpace E] {z₀ z₁ : ℂ} {p₀ p₁ : Path z₀ z₁} (h : p₀.Homotopy p₁)
  {f : ↑unitInterval → ↑unitInterval → ℂ → E}
  (hf :
    ∀ (t : ↑unitInterval), TauCeti.IsAnalyticContinuationAlong (f t) (fun x => h (t, x)) Set.univ)
  (hstart : ∀ (t : ↑unitInterval), f t 0 =ᶠ[nhds z₀] f 0 0) (t : ↑unitInterval) :
  f t 1 =ᶠ[nhds z₁] f 0 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The monodromy theorem for a free homotopy of paths](the-monodromy-theorem-for-a-free-homotopy-of-pat.md)
- [The monodromy theorem for a simply connected domain](the-monodromy-theorem-for-a-simply-connected-dom.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.monodromy_theorem`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Monodromy.html#TauCeti.monodromy_theorem).

## Other forms

**The monodromy theorem, in two-way form.** Formalized in Tau Ceti as [`TauCeti.continuesInside_iff_exists_analyticOnNhd`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/GlobalBranch.html#TauCeti.continuesInside_iff_exists_analyticOnNhd).

```lean
TauCeti.continuesInside_iff_exists_analyticOnNhd.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] [CompleteSpace E] {U : Set ℂ} {z₀ : ℂ} {f₀ : ℂ → E} (hUo : IsOpen U)
  (hUc : IsSimplyConnected U) (hz₀ : z₀ ∈ U) :
  TauCeti.ContinuesInside f₀ U z₀ ↔ ∃ F, AnalyticOnNhd ℂ F U ∧ F =ᶠ[nhds z₀] f₀
```

## Sources

- [Tau Ceti documentation: `TauCeti.monodromy_theorem`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Monodromy.html#TauCeti.monodromy_theorem)
- [Source of `TauCeti.monodromy_theorem` in TauCeti/Analysis/Complex/Conformal/Monodromy.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/Monodromy.lean#L378)
