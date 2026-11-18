---
declaration: module
origin: cited
lean: PhyslibAlpha.Hydrogen.isOpen_normSq_pos, PhyslibAlpha.Hydrogen.differentiableAt_normSq, PhyslibAlpha.Hydrogen.deriv_comp_normSq, PhyslibAlpha.Hydrogen.differentiableAt_comp_normSq, PhyslibAlpha.Hydrogen.deriv_add_apply, PhyslibAlpha.Hydrogen.deriv_mul_apply, PhyslibAlpha.Hydrogen.laplacian_radial_mul, PhyslibAlpha.Hydrogen.hasDerivAt_comp_sqrt
statement: formalized
proof: formalized
---

# The bound-state wave functions of the `d`-dimensional hydrogen atom

The module `PhyslibAlpha.QuantumMechanics.Hydrogen.Eigenfunctions`, [PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean): 22 declarations, 13 with a docstring.

> The bound-state wave functions of the hydrogen atom of physlib in `d ≥ 2` dimensions, as
> explicit eigenfunctions of `-ℏ²/(2m) Δ - k/r` with the Bohr energies `HydrogenAtom.energyLevel`.

## i. Overview

> The angular part is carried by a homogeneous harmonic polynomial `P` of degree `l`
> (`Σᵢ yᵢ ∂ᵢP = l P`, `ΔP = 0`); in three dimensions these are the solid harmonics `r^l Y_lm`. For
> a radial function `f`, the product rule and `Δ‖y‖² = 2d` give, away from the origin,
>
> `Δ(f(r) P) = (f'' + (d - 1 + 2l) f'/r) P`
>
> (`laplacian_radial_mul`, `laplacian_radial_harmonic`). This is the separation of variables in
> spherical coordinates written without angles. The radial factor
> `f(r) = e^(-κr) L_N^(2l+d-2)(2κr)` satisfies
> `r f'' + (2l + d - 1) f' + (2κ(N + l + (d - 1)/2) - κ² r) f = 0` by the Laguerre equation
> (`radialFactor_ode`). With `κ = 1/(a L)`, `a = ℏ²/(m k)` and `L = N + l + (d - 1)/2` the
> Schrödinger equation holds with energy `-ℏ²κ²/(2m) = -Ry/L²`, physlib's Bohr level
> `HydrogenAtom.energyLevel (N + l)` (`boundState_eigen`). The `s` and `p` states are spelled out
> with `P = 1` and `P = yⱼ`.
>
> The equation is proved pointwise away from the nucleus, where `ψ` is smooth. It does not say
> that these are all eigenfunctions, nor that they lie in the domain of the self-adjoint
> Hamiltonian; …

## ii. Key results

> - `laplacian_radial_mul`: the Laplacian of `G(‖y‖²) P(y)`.
> - `laplacian_radial_harmonic`: the radial reduction for homogeneous harmonic `P`.
> - `radialFactor_ode`: the radial equation of `e^(-κr) L_N^(α)(2κr)`.
> - `boundState_eigen`: the bound states and their energies `E_{N+l}`.
> - `boundState_eigen_s`, `boundState_eigen_p`: the `s` and `p` states.

## iv. References

> - H. A. Bethe and E. E. Salpeter, *Quantum Mechanics of One- and Two-Electron Atoms*, Springer
>   (1957).
> - J. J. Sakurai and J. Napolitano, *Modern Quantum Mechanics*, 3rd ed., Cambridge University
>   Press (2020), section 3.7.

## A. The Laplacian of a radial function times a polynomial

**`PhyslibAlpha.Hydrogen.isOpen_normSq_pos`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean#L75).

```lean
lemma isOpen_normSq_pos : IsOpen {y : Space d | 0 < ‖y‖ ^ 2}
```

**`PhyslibAlpha.Hydrogen.differentiableAt_normSq`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean#L78).

```lean
lemma differentiableAt_normSq (x : Space d) : DifferentiableAt ℝ (fun y : Space d => ‖y‖ ^ 2) x
```

**`PhyslibAlpha.Hydrogen.deriv_comp_normSq`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean#L82).

> `∂ᵢ G(‖y‖²) = G'(‖y‖²) 2 yᵢ`.

```lean
lemma deriv_comp_normSq {G : ℝ → ℝ} {g : ℝ} {x : Space d} (hG : HasDerivAt G g (‖x‖ ^ 2))
    (i : Fin d) : ∂[i] (fun y : Space d => G (‖y‖ ^ 2)) x = g * (2 * x i)
```

**`PhyslibAlpha.Hydrogen.differentiableAt_comp_normSq`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean#L92).

```lean
lemma differentiableAt_comp_normSq {G : ℝ → ℝ} {g : ℝ} {x : Space d}
    (hG : HasDerivAt G g (‖x‖ ^ 2)) : DifferentiableAt ℝ (fun y : Space d => G (‖y‖ ^ 2)) x
```

**`PhyslibAlpha.Hydrogen.deriv_add_apply`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean#L96).

```lean
lemma deriv_add_apply {A B : Space d → ℝ} {x : Space d} (hA : DifferentiableAt ℝ A x)
    (hB : DifferentiableAt ℝ B x) (i : Fin d) :
    ∂[i] (fun y => A y + B y) x = ∂[i] A x + ∂[i] B x
```

**`PhyslibAlpha.Hydrogen.deriv_mul_apply`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean#L103).

```lean
lemma deriv_mul_apply {A B : Space d → ℝ} {x : Space d} (hA : DifferentiableAt ℝ A x)
    (hB : DifferentiableAt ℝ B x) (i : Fin d) :
    ∂[i] (fun y => A y * B y) x = A x * ∂[i] B x + B x * ∂[i] A x
```

**`PhyslibAlpha.Hydrogen.laplacian_radial_mul`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean#L111).

> **The Laplacian of `G(‖y‖²) P(y)`** away from the origin:
> `Δ(G P) = G ΔP + 4 G' Σᵢ yᵢ ∂ᵢP + (2d G' + 4‖y‖² G'') P`.

```lean
lemma laplacian_radial_mul {G G' G'' : ℝ → ℝ} (hG : ∀ s, 0 < s → HasDerivAt G (G' s) s)
    (hG' : ∀ s, 0 < s → HasDerivAt G' (G'' s) s) {P : Space d → ℝ} (hP : ContDiff ℝ 2 P)
    {x : Space d} (hx : x ≠ 0) :
    Δ (fun y => G (‖y‖ ^ 2) * P y) x = G (‖x‖ ^ 2) * Δ P x +
      4 * G' (‖x‖ ^ 2) * ∑ i, x i * ∂[i] P x +
        (2 * d * G' (‖x‖ ^ 2) + 4 * ‖x‖ ^ 2 * G'' (‖x‖ ^ 2)) * P x
```

## B. Radial functions of `‖y‖`

**`PhyslibAlpha.Hydrogen.hasDerivAt_comp_sqrt`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean#L163).

```lean
lemma hasDerivAt_comp_sqrt {f f' : ℝ → ℝ} (hf : ∀ r, 0 < r → HasDerivAt f (f' r) r) {s : ℝ}
    (hs : 0 < s) :
    HasDerivAt (fun s => f (Real.sqrt s)) (f' (Real.sqrt s) / (2 * Real.sqrt s)) s
```

**`PhyslibAlpha.Hydrogen.hasDerivAt_comp_sqrt'`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean#L170).

```lean
lemma hasDerivAt_comp_sqrt' {f' f'' : ℝ → ℝ} (hf : ∀ r, 0 < r → HasDerivAt f' (f'' r) r) {s : ℝ}
    (hs : 0 < s) : HasDerivAt (fun s => f' (Real.sqrt s) / (2 * Real.sqrt s))
      ((f'' (Real.sqrt s) - f' (Real.sqrt s) / Real.sqrt s) / (4 * s)) s
```

**`PhyslibAlpha.Hydrogen.laplacian_radial_harmonic`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean#L185).

> The Laplacian of `f(‖y‖) P(y)` for a homogeneous harmonic polynomial `P` of degree `l`:
> `Δ(f P) = (f'' + (d - 1 + 2l) f'/r) P`.

```lean
lemma laplacian_radial_harmonic {f f' f'' : ℝ → ℝ} (hf : ∀ r, 0 < r → HasDerivAt f (f' r) r)
    (hf' : ∀ r, 0 < r → HasDerivAt f' (f'' r) r) {P : Space d → ℝ} (hP : ContDiff ℝ 2 P) {l : ℕ}
    (hE : ∀ y : Space d, ∑ i, y i * ∂[i] P y = l * P y) (hΔ : ∀ y, Δ P y = 0) {x : Space d}
    (hx : x ≠ 0) :
    Δ (fun y => f ‖y‖ * P y) x =
      (f'' ‖x‖ + ((d : ℝ) - 1 + 2 * l) * f' ‖x‖ / ‖x‖) * P x
```

## C. The radial factor

**`PhyslibAlpha.Hydrogen.laguerreScaled`**, a def, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean#L208).

> The polynomial `L_N^(α)(2κr)` in `r`.

```lean
def laguerreScaled (κ : ℝ) (N α : ℕ) : ℝ[X]
```

**`PhyslibAlpha.Hydrogen.radialFactor`**, a def, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean#L211).

> The radial factor `e^(-κr) L_N^(α)(2κr)` of a bound state.

```lean
def radialFactor (κ : ℝ) (N α : ℕ) (r : ℝ) : ℝ
```

**`PhyslibAlpha.Hydrogen.radialFactor'`**, a def, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean#L215).

> The first derivative of `radialFactor`.

```lean
def radialFactor' (κ : ℝ) (N α : ℕ) (r : ℝ) : ℝ
```

**`PhyslibAlpha.Hydrogen.radialFactor''`**, a def, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean#L219).

> The second derivative of `radialFactor`.

```lean
def radialFactor'' (κ : ℝ) (N α : ℕ) (r : ℝ) : ℝ
```

**`PhyslibAlpha.Hydrogen.hasDerivAt_radialFactor`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean#L224).

```lean
lemma hasDerivAt_radialFactor (κ : ℝ) (N α : ℕ) (r : ℝ) :
    HasDerivAt (radialFactor κ N α) (radialFactor' κ N α r) r
```

**`PhyslibAlpha.Hydrogen.hasDerivAt_radialFactor'`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean#L228).

```lean
lemma hasDerivAt_radialFactor' (κ : ℝ) (N α : ℕ) (r : ℝ) :
    HasDerivAt (radialFactor' κ N α) (radialFactor'' κ N α r) r
```

**`PhyslibAlpha.Hydrogen.radialFactor_ode`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean#L234).

> The radial equation of the bound state:
> `r f'' + (α + 1) f' + (2κ(N + (α + 1)/2) - κ² r) f = 0`.

```lean
lemma radialFactor_ode (κ : ℝ) (N α : ℕ) (r : ℝ) :
    r * radialFactor'' κ N α r + ((α : ℝ) + 1) * radialFactor' κ N α r +
      (2 * κ * ((N : ℝ) + ((α : ℝ) + 1) / 2) - κ ^ 2 * r) * radialFactor κ N α r = 0
```

## D. The bound states of the `d`-dimensional hydrogen atom

**`PhyslibAlpha.Hydrogen.boundKappa`**, a def, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean#L252).

> The decay constant `κ = 1/(a L_n)` of the level `n`, with `L_n = n + (d - 1)/2`.

```lean
def boundKappa (H : HydrogenAtom d) (n : ℕ) : ℝ
```

**`PhyslibAlpha.Hydrogen.boundState`**, a def, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean#L256).

> The bound state `ψ(y) = e^(-κ r) L_N^(2l+d-2)(2κ r) P(y)`, `r = ‖y‖`, of the level
> `n = N + l`, built from a homogeneous harmonic polynomial `P` of degree `l`.

```lean
def boundState (H : HydrogenAtom d) (N l : ℕ) (P : Space d → ℝ) (y : Space d) : ℝ
```

**`PhyslibAlpha.Hydrogen.boundState_eigen`**, a lemma, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean#L264).

> **Bound states of the hydrogen atom in `d ≥ 2` dimensions.** Let `P` be a homogeneous
> (`Σᵢ yᵢ ∂ᵢP = l P`) harmonic (`ΔP = 0`) polynomial of degree `l`, for instance `r^l Y_lm` in
> three dimensions. Then away from the nucleus
> `-ℏ²/(2m) Δψ - (k/r) ψ = E_{N+l} ψ` for `ψ = boundState H N l P`, where `E_n` is the Bohr level
> `HydrogenAtom.energyLevel n = -Ry/(n + (d - 1)/2)²`.

```lean
lemma boundState_eigen (H : HydrogenAtom d) (hd : 2 ≤ d) (hk : 0 < H.k) (N l : ℕ)
    {P : Space d → ℝ} (hP : ContDiff ℝ 2 P) (hE : ∀ y : Space d, ∑ i, y i * ∂[i] P y = l * P y)
    (hΔ : ∀ y, Δ P y = 0) {x : Space d} (hx : x ≠ 0) :
    -((ℏ : ℝ) ^ 2 / (2 * H.m)) * Δ (boundState H N l P) x + H.potential x * boundState H N l P x =
      H.energyLevel (N + l) * boundState H N l P x
```

**`PhyslibAlpha.Hydrogen.boundState_eigen_s`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean#L299).

> The constant polynomial is homogeneous of degree `0` and harmonic: the `s` states.

```lean
lemma boundState_eigen_s (H : HydrogenAtom d) (hd : 2 ≤ d) (hk : 0 < H.k) (N : ℕ)
    {x : Space d} (hx : x ≠ 0) :
    -((ℏ : ℝ) ^ 2 / (2 * H.m)) * Δ (boundState H N 0 fun _ => 1) x +
        H.potential x * boundState H N 0 (fun _ => 1) x =
      H.energyLevel N * boundState H N 0 (fun _ => 1) x
```

**`PhyslibAlpha.Hydrogen.boundState_eigen_p`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean#L314).

> A coordinate `yⱼ` is homogeneous of degree `1` and harmonic: the `p` states.

```lean
lemma boundState_eigen_p (H : HydrogenAtom d) (hd : 2 ≤ d) (hk : 0 < H.k) (N : ℕ) (j : Fin d)
    {x : Space d} (hx : x ≠ 0) :
    -((ℏ : ℝ) ^ 2 / (2 * H.m)) * Δ (boundState H N 1 fun y => y j) x +
        H.potential x * boundState H N 1 (fun y => y j) x =
      H.energyLevel (N + 1) * boundState H N 1 (fun y => y j) x
```

## Depends on

- [The Laplacian operator on `Space d`](../../../physlib/spaceandtime/space/part-01/derivatives-laplacian.md)
- [The radial functions of the hydrogen atom](radialfunctions.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Eigenfunctions.lean)
