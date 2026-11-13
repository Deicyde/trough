---
declaration: module
origin: cited
lean: CondensedMatter.TightBindingChain.CubeHilbertSpace, CondensedMatter.TightBindingChain.CubeOperators, CondensedMatter.TightBindingChain.alongX, CondensedMatter.TightBindingChain.alongY, CondensedMatter.TightBindingChain.alongZ, CondensedMatter.TightBindingChain.bracket_alongX_alongY, CondensedMatter.TightBindingChain.bracket_alongX_alongZ, CondensedMatter.TightBindingChain.bracket_alongY_alongZ
statement: formalized
proof: formalized
---

# The open tight binding cube

The module `PhyslibAlpha.CondensedMatter.TightBindingChain.Cube.Basic`, [PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean): 44 declarations, 34 with a docstring; 5 private, not shown.

## i. Overview

> Three open tight binding chains `Tx`, `Ty`, `Tz` along the axes of a cube give the sites
> `(nx, ny, nz)` and the Hilbert space `𝓗[Fin Nx × Fin Ny × Fin Nz]`. Each observable of a chain
> acts on its own axis and leaves the other two in place. Observables of different axes commute:
> only the Hamiltonian and the position of the same axis fail to commute.
>
> In the maximal current state of the cube, the product of the maximal current states of the three
> chains, each axis carries the constant `C` of its own chain. The energy–position uncertainty
> relation of an axis is an equality exactly when that axis has `2` or `3` sites, and it is strict
> from `4` sites on, on the three axes at once.
>
> The six observables `(H, X)` of the three axes satisfy Robertson's relation `|det Ω| ≤ det Σ` in
> every state of the cube. Since different axes commute, `Ω` is block diagonal and `|det Ω|` is the
> product of the squared brackets of the three axes. In the maximal current state `Σ` is block
> diagonal too, and `det Σ / |det Ω|` is the product of the squares of the three constants
> `C`, so the relation is strict from `4 × 4 × 4` on.

## ii. Key results

> - `alongX`, `alongY`, `alongZ` : an observable of a chain acting on its axis of the cube.
> - `bracket_alongX_alongY`, `bracket_alongX_alongZ`, `bracket_alongY_alongZ` : different axes
>   commute.
> - `maxCurrentCubeState` : the maximal current state of the cube.
> - `uncertaintyRatio_alongX`, `uncertaintyRatio_alongY`, `uncertaintyRatio_alongZ` : each axis
>   carries its own `C`.
> - `centeredGramDefect_alongX_eq_zero_iff` (and `Y`, `Z`) : saturation on an axis iff it has `2`
>   or `3` sites.
> - `robertson_schrodinger_cube` : from `4 × 4 × 4` on, strict on the three axes.
> - `cubePairs` : the six observables `(H, X)` of the three axes.
> - `bracketMatrix_cubePairs` : in every state `Ω` is block diagonal, one block per axis.
> - `robertson_det_cube` : Robertson's relation for the six observables, in every state.
> - `covarianceMatrix_maxCurrentCubeState` : in the maximal current state `Σ` is block diagonal.
> - `det_covarianceMatrix_maxCurrentCubeState` : `det Σ = (C(x) C(y) C(z))² |det Ω|`.
> - `robertson_det_maxCurrentCubeState_strict` : from `4 × 4 × 4` on, `|det Ω| < det Σ`.

## iv. References

> * https://www.damtp.cam.ac.uk/user/tong/aqm/aqmtwo.pdf. [ref: tong\_statistical\_physics]

## A. Observables along the axes

**`CondensedMatter.TightBindingChain.CubeHilbertSpace`**, an abbrev, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L80).

> The Hilbert space of the cube: states on the sites `(nx, ny, nz)`.

```lean
abbrev CubeHilbertSpace
```

**`CondensedMatter.TightBindingChain.CubeOperators`**, an abbrev, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L83).

> The operators on the Hilbert space of the cube.

```lean
abbrev CubeOperators
```

**`CondensedMatter.TightBindingChain.alongX`**, an abbrev, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L86).

> An observable of the chain `Tx` acting on the `x` axis of the cube.

```lean
noncomputable abbrev alongX (a : Observable (Tx.HilbertSpace →L[ℂ] Tx.HilbertSpace)) :
    Observable (Tx.CubeOperators Ty Tz)
```

**`CondensedMatter.TightBindingChain.alongY`**, an abbrev, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L91).

> An observable of the chain `Ty` acting on the `y` axis of the cube.

```lean
noncomputable abbrev alongY (b : Observable (Ty.HilbertSpace →L[ℂ] Ty.HilbertSpace)) :
    Observable (Tx.CubeOperators Ty Tz)
```

**`CondensedMatter.TightBindingChain.alongZ`**, an abbrev, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L96).

> An observable of the chain `Tz` acting on the `z` axis of the cube.

```lean
noncomputable abbrev alongZ (c : Observable (Tz.HilbertSpace →L[ℂ] Tz.HilbertSpace)) :
    Observable (Tx.CubeOperators Ty Tz)
```

## B. Different axes commute

**`CondensedMatter.TightBindingChain.bracket_alongX_alongY`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L114).

> Observables of the `x` and `y` axes commute.

```lean
lemma bracket_alongX_alongY (a : Observable (Tx.HilbertSpace →L[ℂ] Tx.HilbertSpace))
    (b : Observable (Ty.HilbertSpace →L[ℂ] Ty.HilbertSpace)) :
    ⁅Tx.alongX Ty Tz a, Tx.alongY Ty Tz b⁆ = 0
```

**`CondensedMatter.TightBindingChain.bracket_alongX_alongZ`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L121).

> Observables of the `x` and `z` axes commute.

```lean
lemma bracket_alongX_alongZ (a : Observable (Tx.HilbertSpace →L[ℂ] Tx.HilbertSpace))
    (c : Observable (Tz.HilbertSpace →L[ℂ] Tz.HilbertSpace)) :
    ⁅Tx.alongX Ty Tz a, Tx.alongZ Ty Tz c⁆ = 0
```

**`CondensedMatter.TightBindingChain.bracket_alongY_alongZ`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L128).

> Observables of the `y` and `z` axes commute.

```lean
lemma bracket_alongY_alongZ (b : Observable (Ty.HilbertSpace →L[ℂ] Ty.HilbertSpace))
    (c : Observable (Tz.HilbertSpace →L[ℂ] Tz.HilbertSpace)) :
    ⁅Tx.alongY Ty Tz b, Tx.alongZ Ty Tz c⁆ = 0
```

## C. The maximal current state of the cube

**`CondensedMatter.TightBindingChain.maxCurrentCubeState`**, a def, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L145).

> The maximal current state of the cube, the product of those of the three chains.

```lean
noncomputable def maxCurrentCubeState : Tx.CubeHilbertSpace Ty Tz
```

**`CondensedMatter.TightBindingChain.norm_maxCurrentCubeState`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L148).

```lean
lemma norm_maxCurrentCubeState : ‖Tx.maxCurrentCubeState Ty Tz‖ = 1
```

**`CondensedMatter.TightBindingChain.maxCurrentCubeVectorState`**, an abbrev, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L153).

> The maximal current state of the cube as a state on its operators.

```lean
noncomputable abbrev maxCurrentCubeVectorState : 𝓢[ℂ, Tx.CubeOperators Ty Tz]
```

## D. The uncertainty relation along each axis

**`CondensedMatter.TightBindingChain.variance_alongX`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L169).

> Along `x`, the cube sees the statistics of the chain `Tx`.

```lean
lemma variance_alongX :
    variance (Tx.maxCurrentCubeVectorState Ty Tz) (Tx.alongX Ty Tz a) =
      variance Tx.maxCurrentVectorState a
```

**`CondensedMatter.TightBindingChain.centeredGramDefect_alongX`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L175).

```lean
lemma centeredGramDefect_alongX :
    centeredGramDefect (Tx.maxCurrentCubeVectorState Ty Tz) (Tx.alongX Ty Tz a)
      (Tx.alongX Ty Tz b) = centeredGramDefect Tx.maxCurrentVectorState a b
```

**`CondensedMatter.TightBindingChain.variance_alongY`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L182).

> Along `y`, the cube sees the statistics of the chain `Ty`.

```lean
lemma variance_alongY :
    variance (Tx.maxCurrentCubeVectorState Ty Tz) (Tx.alongY Ty Tz b') =
      variance Ty.maxCurrentVectorState b'
```

**`CondensedMatter.TightBindingChain.centeredGramDefect_alongY`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L189).

```lean
lemma centeredGramDefect_alongY :
    centeredGramDefect (Tx.maxCurrentCubeVectorState Ty Tz) (Tx.alongY Ty Tz b')
      (Tx.alongY Ty Tz c') = centeredGramDefect Ty.maxCurrentVectorState b' c'
```

**`CondensedMatter.TightBindingChain.variance_alongZ`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L197).

> Along `z`, the cube sees the statistics of the chain `Tz`.

```lean
lemma variance_alongZ :
    variance (Tx.maxCurrentCubeVectorState Ty Tz) (Tx.alongZ Ty Tz b'') =
      variance Tz.maxCurrentVectorState b''
```

**`CondensedMatter.TightBindingChain.centeredGramDefect_alongZ`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L204).

```lean
lemma centeredGramDefect_alongZ :
    centeredGramDefect (Tx.maxCurrentCubeVectorState Ty Tz) (Tx.alongZ Ty Tz b'')
      (Tx.alongZ Ty Tz c'') = centeredGramDefect Tz.maxCurrentVectorState b'' c''
```

**`CondensedMatter.TightBindingChain.uncertaintyRatio_alongX`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L214).

> The `x` axis of the cube carries the constant `C` of the chain `Tx`.

```lean
lemma uncertaintyRatio_alongX :
    √(variance (Tx.maxCurrentCubeVectorState Ty Tz) (Tx.alongX Ty Tz Tx.openHamiltonianObservable) *
      variance (Tx.maxCurrentCubeVectorState Ty Tz) (Tx.alongX Ty Tz Tx.positionObservable)) /
        |Tx.a * Tx.t * Real.cos (Real.pi / (Tx.N + 1))| = Tx.uncertaintyRatio
```

**`CondensedMatter.TightBindingChain.uncertaintyRatio_alongY`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L221).

> The `y` axis of the cube carries the constant `C` of the chain `Ty`.

```lean
lemma uncertaintyRatio_alongY :
    √(variance (Tx.maxCurrentCubeVectorState Ty Tz) (Tx.alongY Ty Tz Ty.openHamiltonianObservable) *
      variance (Tx.maxCurrentCubeVectorState Ty Tz) (Tx.alongY Ty Tz Ty.positionObservable)) /
        |Ty.a * Ty.t * Real.cos (Real.pi / (Ty.N + 1))| = Ty.uncertaintyRatio
```

**`CondensedMatter.TightBindingChain.uncertaintyRatio_alongZ`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L228).

> The `z` axis of the cube carries the constant `C` of the chain `Tz`.

```lean
lemma uncertaintyRatio_alongZ :
    √(variance (Tx.maxCurrentCubeVectorState Ty Tz) (Tx.alongZ Ty Tz Tz.openHamiltonianObservable) *
      variance (Tx.maxCurrentCubeVectorState Ty Tz) (Tx.alongZ Ty Tz Tz.positionObservable)) /
        |Tz.a * Tz.t * Real.cos (Real.pi / (Tz.N + 1))| = Tz.uncertaintyRatio
```

**`CondensedMatter.TightBindingChain.centeredGramDefect_alongX_eq_zero_iff`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L236).

> Along `x`, the centered Gram defect vanishes, that is the uncertainty relation is an
> equality, iff the axis has `2` or `3` sites.

```lean
lemma centeredGramDefect_alongX_eq_zero_iff (ht : Tx.t ≠ 0) (hN : 2 ≤ Tx.N) :
    centeredGramDefect (Tx.maxCurrentCubeVectorState Ty Tz)
      (Tx.alongX Ty Tz Tx.openHamiltonianObservable) (Tx.alongX Ty Tz Tx.positionObservable) = 0 ↔
      Tx.N = 2 ∨ Tx.N = 3
```

**`CondensedMatter.TightBindingChain.centeredGramDefect_alongY_eq_zero_iff`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L244).

> Along `y`, the uncertainty relation is an equality iff the axis has `2` or `3` sites.

```lean
lemma centeredGramDefect_alongY_eq_zero_iff (ht : Ty.t ≠ 0) (hN : 2 ≤ Ty.N) :
    centeredGramDefect (Tx.maxCurrentCubeVectorState Ty Tz)
      (Tx.alongY Ty Tz Ty.openHamiltonianObservable) (Tx.alongY Ty Tz Ty.positionObservable) = 0 ↔
      Ty.N = 2 ∨ Ty.N = 3
```

**`CondensedMatter.TightBindingChain.centeredGramDefect_alongZ_eq_zero_iff`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L252).

> Along `z`, the uncertainty relation is an equality iff the axis has `2` or `3` sites.

```lean
lemma centeredGramDefect_alongZ_eq_zero_iff (ht : Tz.t ≠ 0) (hN : 2 ≤ Tz.N) :
    centeredGramDefect (Tx.maxCurrentCubeVectorState Ty Tz)
      (Tx.alongZ Ty Tz Tz.openHamiltonianObservable) (Tx.alongZ Ty Tz Tz.positionObservable) = 0 ↔
      Tz.N = 2 ∨ Tz.N = 3
```

**`CondensedMatter.TightBindingChain.robertson_schrodinger_cube`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L262).

> Robertson–Schrödinger on the cube. From `4 × 4 × 4` on, the uncertainty relation of
> the maximal current state is strict on the three axes at once: the centered Gram defect of each
> axis is positive.

```lean
lemma robertson_schrodinger_cube (hx : Tx.t ≠ 0) (hy : Ty.t ≠ 0) (hz : Tz.t ≠ 0)
    (hNx : 4 ≤ Tx.N) (hNy : 4 ≤ Ty.N) (hNz : 4 ≤ Tz.N) :
    0 < centeredGramDefect (Tx.maxCurrentCubeVectorState Ty Tz)
        (Tx.alongX Ty Tz Tx.openHamiltonianObservable) (Tx.alongX Ty Tz Tx.positionObservable) ∧
      0 < centeredGramDefect (Tx.maxCurrentCubeVectorState Ty Tz)
        (Tx.alongY Ty Tz Ty.openHamiltonianObservable) (Tx.alongY Ty Tz Ty.positionObservable) ∧
      0 < centeredGramDefect (Tx.maxCurrentCubeVectorState Ty Tz)
        (Tx.alongZ Ty Tz Tz.openHamiltonianObservable) (Tx.alongZ Ty Tz Tz.positionObservable)
```

## E. Robertson's relation for the six observables of the cube

**`CondensedMatter.TightBindingChain.conjugatePair`**, a def, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L289).

> The conjugate pair of a chain: its Hamiltonian and its position.

```lean
noncomputable def conjugatePair (T : TightBindingChain) :
    Fin 2 → Observable (T.HilbertSpace →L[ℂ] T.HilbertSpace)
```

**`CondensedMatter.TightBindingChain.cubePairs`**, a def, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L295).

> The six observables of the cube, the conjugate pair `(H, X)` of each axis: `(j, k)` is the
> `j`-th member of the pair of the axis `k`.

```lean
noncomputable def cubePairs : Fin 2 × Fin 3 → Observable (Tx.CubeOperators Ty Tz)
```

**`CondensedMatter.TightBindingChain.axisBracket`**, a def, [line 300](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L300).

> The expectation `ω⟨⁅H, X⁆⟩` of the bracket of the pair of the axis `k`.

```lean
noncomputable def axisBracket (ω : 𝓢[ℂ, Tx.CubeOperators Ty Tz]) (k : Fin 3) : ℝ
```

**`CondensedMatter.TightBindingChain.cubePairs_x`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L304).

```lean
lemma cubePairs_x (j : Fin 2) :
    Tx.cubePairs Ty Tz (j, 0) = Tx.alongX Ty Tz (Tx.conjugatePair j)
```

**`CondensedMatter.TightBindingChain.cubePairs_y`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L308).

```lean
lemma cubePairs_y (j : Fin 2) :
    Tx.cubePairs Ty Tz (j, 1) = Tx.alongY Ty Tz (Ty.conjugatePair j)
```

**`CondensedMatter.TightBindingChain.cubePairs_z`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L312).

```lean
lemma cubePairs_z (j : Fin 2) :
    Tx.cubePairs Ty Tz (j, 2) = Tx.alongZ Ty Tz (Tz.conjugatePair j)
```

**`CondensedMatter.TightBindingChain.bracket_cubePairs_of_ne`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L325).

> Observables of different axes of the cube commute.

```lean
lemma bracket_cubePairs_of_ne {p q : Fin 2 × Fin 3} (h : p.2 ≠ q.2) :
    ⁅Tx.cubePairs Ty Tz p, Tx.cubePairs Ty Tz q⁆ = 0
```

**`CondensedMatter.TightBindingChain.bracketMatrix_cubePairs`**, a lemma, [line 352](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L352).

> In every state of the cube the bracket matrix `Ω` of the six observables is block diagonal,
> one antisymmetric `2 × 2` block per axis.

```lean
lemma bracketMatrix_cubePairs (ω : 𝓢[ℂ, Tx.CubeOperators Ty Tz]) :
    bracketMatrix ω (Tx.cubePairs Ty Tz) =
      blockDiagonal fun k => !![0, Tx.axisBracket Ty Tz ω k; -Tx.axisBracket Ty Tz ω k, 0]
```

**`CondensedMatter.TightBindingChain.robertson_det_cube`**, a lemma, [line 372](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L372).

> **Robertson's relation on the cube.** In every state of the cube the volume `det Σ` of the
> dispersion of the six observables is at least the product of the squared brackets of the three
> axes.

```lean
lemma robertson_det_cube (ω : 𝓢[ℂ, Tx.CubeOperators Ty Tz]) :
    (Tx.axisBracket Ty Tz ω 0 * Tx.axisBracket Ty Tz ω 1 * Tx.axisBracket Ty Tz ω 2) ^ 2 ≤
      (covarianceMatrix ω (Tx.cubePairs Ty Tz)).det
```

## F. Robertson's relation in the maximal current state of the cube

**`CondensedMatter.TightBindingChain.covariance_alongX`**, a lemma, [line 394](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L394).

```lean
lemma covariance_alongX :
    covariance (Tx.maxCurrentCubeVectorState Ty Tz) (Tx.alongX Ty Tz a) (Tx.alongX Ty Tz b) =
      covariance Tx.maxCurrentVectorState a b
```

**`CondensedMatter.TightBindingChain.covariance_alongY`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L400).

```lean
lemma covariance_alongY :
    covariance (Tx.maxCurrentCubeVectorState Ty Tz) (Tx.alongY Ty Tz b') (Tx.alongY Ty Tz c') =
      covariance Ty.maxCurrentVectorState b' c'
```

**`CondensedMatter.TightBindingChain.covariance_alongZ`**, a lemma, [line 407](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L407).

```lean
lemma covariance_alongZ :
    covariance (Tx.maxCurrentCubeVectorState Ty Tz) (Tx.alongZ Ty Tz b'') (Tx.alongZ Ty Tz c'') =
      covariance Tz.maxCurrentVectorState b'' c''
```

**`CondensedMatter.TightBindingChain.covariance_alongX_alongY`**, a lemma, [line 415](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L415).

> In the maximal current state of the cube the `x` and `y` axes are uncorrelated.

```lean
lemma covariance_alongX_alongY :
    covariance (Tx.maxCurrentCubeVectorState Ty Tz) (Tx.alongX Ty Tz a) (Tx.alongY Ty Tz b') = 0
```

**`CondensedMatter.TightBindingChain.covariance_alongX_alongZ`**, a lemma, [line 421](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L421).

> In the maximal current state of the cube the `x` and `z` axes are uncorrelated.

```lean
lemma covariance_alongX_alongZ :
    covariance (Tx.maxCurrentCubeVectorState Ty Tz) (Tx.alongX Ty Tz a) (Tx.alongZ Ty Tz b'') = 0
```

**`CondensedMatter.TightBindingChain.covariance_alongY_alongZ`**, a lemma, [line 427](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L427).

> In the maximal current state of the cube the `y` and `z` axes are uncorrelated.

```lean
lemma covariance_alongY_alongZ :
    covariance (Tx.maxCurrentCubeVectorState Ty Tz) (Tx.alongY Ty Tz b') (Tx.alongZ Ty Tz b'') =
      0
```

**`CondensedMatter.TightBindingChain.covarianceMatrix_maxCurrentCubeState`**, a lemma, [line 439](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L439).

> In the maximal current state of the cube the covariance matrix `Σ` of the six observables is
> block diagonal, the block of each axis being the covariance matrix of its chain.

```lean
lemma covarianceMatrix_maxCurrentCubeState :
    covarianceMatrix (Tx.maxCurrentCubeVectorState Ty Tz) (Tx.cubePairs Ty Tz) =
      blockDiagonal ![covarianceMatrix Tx.maxCurrentVectorState Tx.conjugatePair,
        covarianceMatrix Ty.maxCurrentVectorState Ty.conjugatePair,
        covarianceMatrix Tz.maxCurrentVectorState Tz.conjugatePair]
```

**`CondensedMatter.TightBindingChain.det_covarianceMatrix_conjugatePair`**, a lemma, [line 466](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L466).

> In the maximal current state of a chain, `det Σ = C² (a t cos (π / (N + 1)))²` for the
> pair `(H, X)`.

```lean
lemma det_covarianceMatrix_conjugatePair (T : TightBindingChain) (ht : T.t ≠ 0) (hN : 2 ≤ T.N) :
    (covarianceMatrix T.maxCurrentVectorState T.conjugatePair).det =
      T.uncertaintyRatio ^ 2 * (T.a * T.t * Real.cos (Real.pi / (T.N + 1))) ^ 2
```

**`CondensedMatter.TightBindingChain.sq_axisBracket_maxCurrentCubeState`**, a lemma, [line 480](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L480).

> In the maximal current state of the cube, the bracket of each axis is that of its chain,
> `± a t cos (π / (N + 1))`.

```lean
lemma sq_axisBracket_maxCurrentCubeState :
    (Tx.axisBracket Ty Tz (Tx.maxCurrentCubeVectorState Ty Tz) 0 *
        Tx.axisBracket Ty Tz (Tx.maxCurrentCubeVectorState Ty Tz) 1 *
        Tx.axisBracket Ty Tz (Tx.maxCurrentCubeVectorState Ty Tz) 2) ^ 2 =
      (Tx.a * Tx.t * Real.cos (Real.pi / (Tx.N + 1)) *
        (Ty.a * Ty.t * Real.cos (Real.pi / (Ty.N + 1))) *
        (Tz.a * Tz.t * Real.cos (Real.pi / (Tz.N + 1)))) ^ 2
```

**`CondensedMatter.TightBindingChain.det_covarianceMatrix_maxCurrentCubeState`**, a lemma, [line 520](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L520).

> In the maximal current state of the cube, `det Σ = C(x)² C(y)² C(z)² |det Ω|`:
> the ratio of the two sides of Robertson's relation is the product of the constants of the three
> axes.

```lean
lemma det_covarianceMatrix_maxCurrentCubeState (hx : Tx.t ≠ 0) (hy : Ty.t ≠ 0) (hz : Tz.t ≠ 0)
    (hNx : 2 ≤ Tx.N) (hNy : 2 ≤ Ty.N) (hNz : 2 ≤ Tz.N) :
    (covarianceMatrix (Tx.maxCurrentCubeVectorState Ty Tz) (Tx.cubePairs Ty Tz)).det =
      (Tx.uncertaintyRatio * Ty.uncertaintyRatio * Tz.uncertaintyRatio) ^ 2 *
        (Tx.axisBracket Ty Tz (Tx.maxCurrentCubeVectorState Ty Tz) 0 *
          Tx.axisBracket Ty Tz (Tx.maxCurrentCubeVectorState Ty Tz) 1 *
          Tx.axisBracket Ty Tz (Tx.maxCurrentCubeVectorState Ty Tz) 2) ^ 2
```

**`CondensedMatter.TightBindingChain.robertson_det_maxCurrentCubeState_strict`**, a lemma, [line 536](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean#L536).

> **Robertson's relation is strict in the maximal current state of the cube.** From
> `4 × 4 × 4` on, `|det Ω| < det Σ` for the six observables of the cube.

```lean
lemma robertson_det_maxCurrentCubeState_strict (hx : Tx.t ≠ 0) (hy : Ty.t ≠ 0)
    (hz : Tz.t ≠ 0) (hNx : 4 ≤ Tx.N) (hNy : 4 ≤ Ty.N) (hNz : 4 ≤ Tz.N) :
    |(bracketMatrix (Tx.maxCurrentCubeVectorState Ty Tz) (Tx.cubePairs Ty Tz)).det| <
      (covarianceMatrix (Tx.maxCurrentCubeVectorState Ty Tz) (Tx.cubePairs Ty Tz)).det
```

## Depends on

- [The elemental uncertainty of the open tight binding chain](maxcurrentstate-uncertaintyratio.md)
- [Product states of a product of finite targets](../../../quantummechanics/hilbertspaces/finitetarget-productstate.md)

## Sources

- [PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/Basic.lean)
