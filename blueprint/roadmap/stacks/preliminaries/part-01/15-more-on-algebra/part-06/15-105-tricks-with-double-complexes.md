---
declaration: section
origin: cited
lean: CplxCplx.total_H0_eq_zero, CplxCplx.Hom.isTotalQuasiIso_of_isInternalQuasiIso
statement: formalized
proof: formalized
---

# 15.105 Tricks with double complexes

Section 15.105 of the Stacks Project, [Tag 0EYW](https://stacks.math.columbia.edu/tag/0EYW). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0H0Q, a lemma

[Tag 0H0Q](https://stacks.math.columbia.edu/tag/0H0Q) in the Stacks Project.

**`CplxCplx.total_H0_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/ProductTotalComplex.lean, line 386](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/ProductTotalComplex.lean#L386).

> **Stacks Tag 0H0Q (Lemma 15.105.1).**
> Let `A_0^• → A_1^• → ⋯` be a complex of complexes of abelian groups such that
> `H^{-p}(A_p^•) = 0` for all `p ≥ 0`.  Then `H^0(Tot_π(A^{•,•})) = 0`, i.e. every
> degree-`0` cocycle of the product total complex is a coboundary: every
> `x ∈ Tot_π^0` with `D^0 x = 0` is `D^{-1} y` for some `y ∈ Tot_π^{-1}`.
> (Together with `D ∘ D = 0`, recorded in `totalD_totalD_eq_zero` below, this says
> exactly that `ker(D^0) = im(D^{-1})`, i.e. `H^0(Tot_π) = 0`.)
>
> Rigorous proof (recursion on `p`; see the block comment above for the math).
> Build, by `Nat.rec`, a dependent stream
> `Y : (p : ℕ) → Σ' (yp : c.A p (-1 - (p:ℤ))), c.StageInvariant x p yp` such that the
> component equation of `D^{-1} (fun p => (Y p).fst) = x` holds at every `p`; set
> `y p := (Y p).fst`.
> * **Base (`Y 0`).**  `d_eq_zero_of_totalD_eq_zero` says `x 0` is a `0`-cocycle, so `hH 0`
>   (after reconciling `0 - ↑0 = -↑0`) yields `w` with
>   `d_2(w) = x_0`; take `(Y 0).fst := w`.  `StageInvariant x 0 w` reduces (`(-1)^0 = 1`) to
>   `f_0(d_2 w) = f_0(x_0)`, immediate from `d_2 w = x_0`.
> * **Step (`Y (p+1)` from `Y p`).**  Let `yp := (Y p).fst`, `hinv := (Y p).snd`.
>   `d_sub_eq_zero_of_stageInvariant c hx hinv` shows `r_{p+1} = x_{p+1} - f_p(yp)` is a
>   `(-(p+1))`-cocycle, so `hH (p+1)` yields `w'` with
>   `d_2(w') = (-1)^{p+1} r_{p+1}` (scale the witness by `(-1)^{p+1}`, valid since
>   `(-1)^{p+1}` is a unit; or equivalently apply `hH` to `(-1)^{p+1} r_{p+1}`,
>   which is also a cocycle).  Take `(Y (p+1)).fst := w'`.  Then `StageInvariant x (p+1) w'`
>   follows because `f\_\{p+1}(d\_2 w') = (-1)^\{p+1} f\_\{p+1}(r\_\{p+1}) =
>   (-1)^\{p+1}(f\_\{p+1}(x\_\{p+1}) - f\_\{p+1}(f\_p yp)) = (-1)^\{p+1} f\_\{p+1}(x\_\{p+1})`
>   using `c.f_f p` (`f_{p+1}∘f_p = 0`).
> Finally `c.totalD (-1) y = x` by `funext p`, `cases p`, reading off the recorded
> construction equations (the `p=0` and `p+1` cases of `totalD_apply_zero` /
> `totalD_apply_succ`, `dPartHom_apply`, `fPartHom_apply`).

```lean
theorem total_H0_eq_zero (c : CplxCplx)
    (hH : ∀ p : ℕ, c.InternalCohomologyVanishes p)
    (x : c.Tot 0) (hx : c.totalD 0 x = 0) :
    ∃ y : c.Tot (-1), c.totalD (-1) y = x
```

## Tag 0EYX, a lemma

[Tag 0EYX](https://stacks.math.columbia.edu/tag/0EYX) in the Stacks Project.

**`CplxCplx.Hom.isTotalQuasiIso_of_isInternalQuasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/ProductTotalComplex/Rowwise.lean, line 611](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/ProductTotalComplex/Rowwise.lean#L611).

> A morphism between complexes of cochain complexes
> which is a quasi-isomorphism on every internal complex induces a quasi-isomorphism between
> their product total complexes.

```lean
theorem isTotalQuasiIso_of_isInternalQuasiIso {c c' : CplxCplx} (g : CplxCplx.Hom c c')
    (hg : g.IsInternalQuasiIso) : g.IsTotalQuasiIso
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.105, Tag 0EYW](https://stacks.math.columbia.edu/tag/0EYW)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
