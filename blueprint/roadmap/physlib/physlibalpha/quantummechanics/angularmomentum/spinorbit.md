---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.AngularMomentumRepresentation.dot, PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jsq_tensor, PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jsq_standard, PhyslibAlpha.Sl2.spinOrbitValue, PhyslibAlpha.Sl2.dot_coupled_stringVec, PhyslibAlpha.Sl2.dot_coupled_stringVec_doublet_upper, PhyslibAlpha.Sl2.dot_coupled_stringVec_doublet_lower, PhyslibAlpha.Sl2.spinOrbitValue_doublet_sub
statement: formalized
proof: formalized
---

# Spin–orbit coupling

The module `PhyslibAlpha.QuantumMechanics.AngularMomentum.SpinOrbit`, [PhyslibAlpha/QuantumMechanics/AngularMomentum/SpinOrbit.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SpinOrbit.lean): 9 declarations, 9 with a docstring.

> The operator `L · S` on coupled angular momenta, its eigenvalues on the states of total angular
> momentum `J`, the fine-structure doublet and Landé's interval rule.

## i. Overview

> For two angular momenta `L` on `V` and `S` on `W` the scalar product
> `L · S = Lx ⊗ Sx + Ly ⊗ Sy + Lz ⊗ Sz` satisfies, for the total angular momentum
> `J = L ⊗ 1 + 1 ⊗ S`,
>
> `J² = L² ⊗ 1 + 1 ⊗ S² + 2 L · S`.
>
> This is pure algebra on pure tensors (`Jsq_tensor`). On `V(m) ⊗ V(n)` with `l = m/2`,
> `s = n/2`, the operators `L²` and `S²` are the scalars `l(l + 1)` and `s(s + 1)`
> (`Jsq_standard`), and `J²` acts on the `k`-th lowering string by `J(J + 1)`,
> `J = l + s - k` (`Jsq_coupled_stringVec`). Hence every state of total angular momentum `J` is an
> eigenvector of `L · S`:
>
> `L · S = (J(J + 1) - l(l + 1) - s(s + 1)) / 2`.
>
> With a spin-orbit Hamiltonian `ζ L · S` this gives
>
> - the fine-structure doublet for `s = 1/2`: `L · S = l/2` for `J = l + 1/2` and
>   `L · S = -(l + 1)/2` for `J = l - 1/2`, a splitting of `(2l + 1)/2` in units of `ζ`;
> - Landé's interval rule: neighbouring levels `J` and `J - 1` of a multiplet are `J` apart in
>   units of `ζ`.

## ii. Key results

> - `dot`, `Jsq_tensor`: the operator `L · S` and the identity `J² = L² + S² + 2 L · S`.
> - `Jsq_standard`: `J² = j(j + 1)` on the spin-`j` representation.
> - `dot_coupled_stringVec`: the eigenvalues of `L · S`.
> - `dot_coupled_stringVec_doublet_upper`, `dot_coupled_stringVec_doublet_lower`: the doublet.
> - `spinOrbitValue_sub_succ`: the interval rule.

## iv. References

> - J. J. Sakurai and J. Napolitano, *Modern Quantum Mechanics*, 3rd ed., Cambridge University
>   Press (2020), sections 3.8 and 5.3.
> - A. Landé, *Termstruktur und Zeemaneffekt der Multipletts*, Z. Phys. 15, 189 (1923).

## A. The scalar product of two angular momenta

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.dot`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SpinOrbit.lean#L83).

> The scalar product `L · S = Lx ⊗ Sx + Ly ⊗ Sy + Lz ⊗ Sz` on `V ⊗ W`.

```lean
def dot (ρ₁ : AngularMomentumRepresentation V) (ρ₂ : AngularMomentumRepresentation W) :
    Module.End ℂ (V ⊗[ℂ] W)
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jsq_tensor`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SpinOrbit.lean#L88).

> **`J² = L² + S² + 2 L · S`.**

```lean
lemma Jsq_tensor (ρ₁ : AngularMomentumRepresentation V) (ρ₂ : AngularMomentumRepresentation W) :
    (tensor ρ₁ ρ₂).Jsq = ρ₁.Jsq.rTensor W + ρ₂.Jsq.lTensor V + (2 : ℂ) • dot ρ₁ ρ₂
```

## B. The Casimir operator of `V(n)`

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jsq_standard`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SpinOrbit.lean#L103).

> `J² = j(j + 1)` on the spin-`j` representation `V(2j)`.

```lean
lemma Jsq_standard (n : ℕ) :
    (standard n).Jsq =
      ((n : ℂ) / 2 * ((n : ℂ) / 2 + 1)) • (1 : Module.End ℂ (StandardSl2Module ℂ n))
```

## C. Eigenvalues of `L · S`

**`PhyslibAlpha.Sl2.spinOrbitValue`**, a def, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SpinOrbit.lean#L126).

> The eigenvalue `(J(J + 1) - l(l + 1) - s(s + 1)) / 2` of `L · S` for `l = m/2`, `s = n/2`
> and `J = (m + n)/2 - k`.

```lean
def spinOrbitValue (m n k : ℕ) : ℂ
```

**`PhyslibAlpha.Sl2.dot_coupled_stringVec`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SpinOrbit.lean#L133).

> **Spin–orbit eigenvalues.** Every vector of the `k`-th lowering string of `V(m) ⊗ V(n)`, a
> state of total angular momentum `J = (m + n)/2 - k`, is an eigenvector of `L · S` with eigenvalue
> `(J(J + 1) - l(l + 1) - s(s + 1)) / 2`.

```lean
lemma dot_coupled_stringVec {k : ℕ} (hmn : 0 < m + n) (hkm : k ≤ m) (hkn : k ≤ n) (l : ℕ) :
    dot (standard m) (standard n) (stringVec m n k l) =
      spinOrbitValue m n k • stringVec m n k l
```

## D. Fine structure and the interval rule

**`PhyslibAlpha.Sl2.dot_coupled_stringVec_doublet_upper`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SpinOrbit.lean#L154).

> **Fine-structure doublet, upper level.** For spin `1/2` and `J = l + 1/2`,
> `L · S = l/2` (`l = m/2`).

```lean
lemma dot_coupled_stringVec_doublet_upper (l' : ℕ) :
    dot (standard m) (standard 1) (stringVec m 1 0 l') =
      ((m : ℂ) / 4) • stringVec m 1 0 l'
```

**`PhyslibAlpha.Sl2.dot_coupled_stringVec_doublet_lower`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SpinOrbit.lean#L164).

> **Fine-structure doublet, lower level.** For spin `1/2` and `J = l - 1/2`,
> `L · S = -(l + 1)/2` (`l = m/2`, `m ≥ 1`).

```lean
lemma dot_coupled_stringVec_doublet_lower (hm : 1 ≤ m) (l' : ℕ) :
    dot (standard m) (standard 1) (stringVec m 1 1 l') =
      (-((m : ℂ) + 2) / 4) • stringVec m 1 1 l'
```

**`PhyslibAlpha.Sl2.spinOrbitValue_doublet_sub`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SpinOrbit.lean#L174).

> The doublet splitting `l/2 + (l + 1)/2 = (2l + 1)/2`.

```lean
lemma spinOrbitValue_doublet_sub (hm : 1 ≤ m) :
    spinOrbitValue m 1 0 - spinOrbitValue m 1 1 = ((m : ℂ) + 1) / 2
```

**`PhyslibAlpha.Sl2.spinOrbitValue_sub_succ`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SpinOrbit.lean#L182).

> **Landé's interval rule.** The levels `J` and `J - 1` of a multiplet differ in `L · S` by `J`,
> `J = (m + n)/2 - k`.

```lean
lemma spinOrbitValue_sub_succ {k : ℕ} (hkm : k + 1 ≤ m) (hkn : k + 1 ≤ n) :
    spinOrbitValue m n k - spinOrbitValue m n (k + 1) = ((m + n - 2 * k : ℕ) : ℂ) / 2
```

## Depends on

- [Addition of angular momenta](addition.md)

## Proof depends on

- [Schur's lemma for the standard sl₂ modules](../../mathematics/part-02/representationtheory/sl2-schur.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/AngularMomentum/SpinOrbit.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/SpinOrbit.lean)
