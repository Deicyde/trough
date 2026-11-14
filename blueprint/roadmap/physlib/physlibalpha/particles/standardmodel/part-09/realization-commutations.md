---
declaration: module
origin: cited
lean: StandardModel.AlgebraRealization.A_comm_A, StandardModel.AlgebraRealization.A_comm_H, StandardModel.AlgebraRealization.A_comm_barH, StandardModel.AlgebraRealization.A_comm_d, StandardModel.AlgebraRealization.A_comm_bard, StandardModel.AlgebraRealization.A_comm_u, StandardModel.AlgebraRealization.A_comm_baru, StandardModel.AlgebraRealization.A_comm_Q
statement: formalized
proof: formalized
---

# The statistics of the Standard Model fields

The module `PhyslibAlpha.Particles.StandardModel.Realization.Commutations`, [PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean): 91 declarations, 91 with a docstring; 1 private, not shown.

## i. Overview

> The thirteen families of derivative symbols of a Standard Model are the jet algebra's own
> families pushed along the defining map, so their statistics are the jet algebra's own
> statistics pushed along the same map. The gauge field is bosonic: its symbols commute with
> each other and with every matter symbol. The Higgs symbols commute with each other and
> with every fermion symbol, and the fermion symbols anticommute among themselves. Together
> these fix the statistics of every symbol of the theory.
>
> Each law is one line: the corresponding jet algebra fact, transported. A commutation
> transports by `Commute.map`, an anticommutation by the private helper `map_anticomm` at
> the head of the section, which is the fourth of the transport shapes of section B of
> [`Basic.lean`](realization-basic.md) and is needed only here. The laws carry the names they carried
> when they were axioms of `AlgebraRealization`, so they are used exactly as before.
>
> These are the last of the laws of the bare symbols; the covariant reduction that uses them
> is [`CovariantDeriv.lean`](realization-covariantderiv.md).

## ii. Key results

> - `AlgebraRealization.A_comm_A`, `AlgebraRealization.A_comm_H` and their companions : the
>   gauge-field symbols commute with every symbol of the theory.
> - `AlgebraRealization.H_comm_H` and its companions : the Higgs symbols commute with each
>   other and with every fermion symbol.
> - `AlgebraRealization.d_anticomm_bard` and its companions : the fermion symbols anticommute
>   among themselves.

## iv. References

> * None.

## A. The statistics of the fields

> The gauge field is bosonic: its symbols commute with each other and with every matter
> symbol. The Higgs symbols commute with each other and with every fermion symbol, and the
> fermion symbols anticommute among themselves. Together these fix the statistics of every
> symbol of the theory.
>
> The commutations are the jet algebra's own, pushed along `toAlgHom` by `Commute.map`. The
> anticommutations need the transport helper that opens the section: the defining map
> preserves products and negation, so an anticommutation in the jet algebra is one in `B`.

**`StandardModel.AlgebraRealization.A_comm_A`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L93).

> The law `A_comm_A` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma A_comm_A : ∀ (s s' : Multiset (Fin 1 ⊕ Fin 3)) (μ μ' : Fin 1 ⊕ Fin 3)
    (ψ ψ' : Module.Dual ℝ GaugeAlgebra), Commute (h.A s μ ψ) (h.A s' μ' ψ')
```

**`StandardModel.AlgebraRealization.A_comm_H`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L99).

> The law `A_comm_H` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma A_comm_H : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ HiggsVec),
    Commute (h.A s μ ψ) (h.H s' φ)
```

**`StandardModel.AlgebraRealization.A_comm_barH`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L106).

> The law `A_comm_barH` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma A_comm_barH : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ
      (ConjModule HiggsVec)),
    Commute (h.A s μ ψ) (h.barH s' φ)
```

**`StandardModel.AlgebraRealization.A_comm_d`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L114).

> The law `A_comm_d` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma A_comm_d : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (s' : Multiset (Fin 1 ⊕ Fin 3))
      (φ : Module.Dual ℂ DownSinglet),
    Commute (h.A s μ ψ) (h.d i s' φ)
```

**`StandardModel.AlgebraRealization.A_comm_bard`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L122).

> The law `A_comm_bard` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma A_comm_bard : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ
      (ConjModule DownSinglet)),
    Commute (h.A s μ ψ) (h.bard i s' φ)
```

**`StandardModel.AlgebraRealization.A_comm_u`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L130).

> The law `A_comm_u` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma A_comm_u : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (s' : Multiset (Fin 1 ⊕ Fin 3))
      (φ : Module.Dual ℂ UpSinglet),
    Commute (h.A s μ ψ) (h.u i s' φ)
```

**`StandardModel.AlgebraRealization.A_comm_baru`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L138).

> The law `A_comm_baru` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma A_comm_baru : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ
      (ConjModule UpSinglet)),
    Commute (h.A s μ ψ) (h.baru i s' φ)
```

**`StandardModel.AlgebraRealization.A_comm_Q`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L146).

> The law `A_comm_Q` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma A_comm_Q : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (s' : Multiset (Fin 1 ⊕ Fin 3))
      (φ : Module.Dual ℂ QuarkDoublet),
    Commute (h.A s μ ψ) (h.Q i s' φ)
```

**`StandardModel.AlgebraRealization.A_comm_barQ`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L154).

> The law `A_comm_barQ` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma A_comm_barQ : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ
      (ConjModule QuarkDoublet)),
    Commute (h.A s μ ψ) (h.barQ i s' φ)
```

**`StandardModel.AlgebraRealization.A_comm_L`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L162).

> The law `A_comm_L` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma A_comm_L : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (s' : Multiset (Fin 1 ⊕ Fin 3))
      (φ : Module.Dual ℂ LeptonDoubletV),
    Commute (h.A s μ ψ) (h.L i s' φ)
```

**`StandardModel.AlgebraRealization.A_comm_barL`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L170).

> The law `A_comm_barL` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma A_comm_barL : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ
      (ConjModule LeptonDoubletV)),
    Commute (h.A s μ ψ) (h.barL i s' φ)
```

**`StandardModel.AlgebraRealization.A_comm_e`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L178).

> The law `A_comm_e` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma A_comm_e : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (s' : Multiset (Fin 1 ⊕ Fin 3))
      (φ : Module.Dual ℂ LeptonSinglet),
    Commute (h.A s μ ψ) (h.e i s' φ)
```

**`StandardModel.AlgebraRealization.A_comm_bare`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L186).

> The law `A_comm_bare` of a Standard Model, obtained from the corresponding law of the
> jet algebra by pushing it along the defining algebra map.

```lean
lemma A_comm_bare : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (i : Fin 3) (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ
      (ConjModule LeptonSinglet)),
    Commute (h.A s μ ψ) (h.bare i s' φ)
```

**`StandardModel.AlgebraRealization.H_comm_H`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L193).

> The Higgs is bosonic: two Higgs symbols commute.

```lean
lemma H_comm_H : ∀ (s s' : Multiset (Fin 1 ⊕ Fin 3)) (φ φ' : Module.Dual ℂ HiggsVec),
    Commute (h.H s φ) (h.H s' φ')
```

**`StandardModel.AlgebraRealization.H_comm_barH`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L199).

> A Higgs symbol commutes with a conjugate Higgs symbol.

```lean
lemma H_comm_barH : ∀ (s s' : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ HiggsVec)
    (φ' : Module.Dual ℂ (ConjModule HiggsVec)),
    Commute (h.H s φ) (h.barH s' φ')
```

**`StandardModel.AlgebraRealization.barH_comm_barH`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L206).

> Two conjugate Higgs symbols commute.

```lean
lemma barH_comm_barH : ∀ (s s' : Multiset (Fin 1 ⊕ Fin 3)) (φ φ' : Module.Dual ℂ
    (ConjModule HiggsVec)),
    Commute (h.barH s φ) (h.barH s' φ')
```

**`StandardModel.AlgebraRealization.H_comm_d`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L214).

> The Higgs symbols commute with the down-type quark symbols: the Higgs is a boson, so it
> carries no statistics against the fermions.

```lean
lemma H_comm_d : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ HiggsVec) (i : Fin 3)
    (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ' : Module.Dual ℂ DownSinglet),
    Commute (h.H s φ) (h.d i s' φ')
```

**`StandardModel.AlgebraRealization.H_comm_bard`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L223).

> The Higgs symbols commute with the conjugate down-type quark symbols: the Higgs is a boson, so
> it carries no statistics against the fermions.

```lean
lemma H_comm_bard : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ HiggsVec) (i : Fin 3)
    (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ' : Module.Dual ℂ (ConjModule DownSinglet)),
    Commute (h.H s φ) (h.bard i s' φ')
```

**`StandardModel.AlgebraRealization.H_comm_u`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L232).

> The Higgs symbols commute with the up-type quark symbols: the Higgs is a boson, so it carries
> no statistics against the fermions.

```lean
lemma H_comm_u : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ HiggsVec) (i : Fin 3)
    (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ' : Module.Dual ℂ UpSinglet),
    Commute (h.H s φ) (h.u i s' φ')
```

**`StandardModel.AlgebraRealization.H_comm_baru`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L241).

> The Higgs symbols commute with the conjugate up-type quark symbols: the Higgs is a boson, so
> it carries no statistics against the fermions.

```lean
lemma H_comm_baru : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ HiggsVec) (i : Fin 3)
    (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ' : Module.Dual ℂ (ConjModule UpSinglet)),
    Commute (h.H s φ) (h.baru i s' φ')
```

**`StandardModel.AlgebraRealization.H_comm_Q`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L250).

> The Higgs symbols commute with the quark doublet symbols: the Higgs is a boson, so it carries
> no statistics against the fermions.

```lean
lemma H_comm_Q : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ HiggsVec) (i : Fin 3)
    (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ' : Module.Dual ℂ QuarkDoublet),
    Commute (h.H s φ) (h.Q i s' φ')
```

**`StandardModel.AlgebraRealization.H_comm_barQ`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L259).

> The Higgs symbols commute with the conjugate quark doublet symbols: the Higgs is a boson, so
> it carries no statistics against the fermions.

```lean
lemma H_comm_barQ : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ HiggsVec) (i : Fin 3)
    (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ' : Module.Dual ℂ (ConjModule QuarkDoublet)),
    Commute (h.H s φ) (h.barQ i s' φ')
```

**`StandardModel.AlgebraRealization.H_comm_L`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L268).

> The Higgs symbols commute with the lepton doublet symbols: the Higgs is a boson, so it carries
> no statistics against the fermions.

```lean
lemma H_comm_L : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ HiggsVec) (i : Fin 3)
    (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ' : Module.Dual ℂ LeptonDoubletV),
    Commute (h.H s φ) (h.L i s' φ')
```

**`StandardModel.AlgebraRealization.H_comm_barL`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L277).

> The Higgs symbols commute with the conjugate lepton doublet symbols: the Higgs is a boson, so
> it carries no statistics against the fermions.

```lean
lemma H_comm_barL : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ HiggsVec) (i : Fin 3)
    (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ' : Module.Dual ℂ (ConjModule LeptonDoubletV)),
    Commute (h.H s φ) (h.barL i s' φ')
```

**`StandardModel.AlgebraRealization.H_comm_e`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L287).

> The Higgs symbols commute with the lepton singlet symbols: the Higgs is a boson, so it carries
> no statistics against the fermions.

```lean
lemma H_comm_e : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ HiggsVec) (i : Fin 3)
    (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ' : Module.Dual ℂ LeptonSinglet),
    Commute (h.H s φ) (h.e i s' φ')
```

**`StandardModel.AlgebraRealization.H_comm_bare`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L296).

> The Higgs symbols commute with the conjugate lepton singlet symbols: the Higgs is a boson, so
> it carries no statistics against the fermions.

```lean
lemma H_comm_bare : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ HiggsVec) (i : Fin 3)
    (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ' : Module.Dual ℂ (ConjModule LeptonSinglet)),
    Commute (h.H s φ) (h.bare i s' φ')
```

**`StandardModel.AlgebraRealization.barH_comm_d`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L306).

> The conjugate Higgs symbols commute with the down-type quark symbols: the Higgs is a boson, so
> it carries no statistics against the fermions.

```lean
lemma barH_comm_d : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule HiggsVec))
    (i : Fin 3) (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ' : Module.Dual ℂ DownSinglet),
    Commute (h.barH s φ) (h.d i s' φ')
```

**`StandardModel.AlgebraRealization.barH_comm_bard`**, a lemma, [line 315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L315).

> The conjugate Higgs symbols commute with the conjugate down-type quark symbols: the Higgs is a
> boson, so it carries no statistics against the fermions.

```lean
lemma barH_comm_bard : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule HiggsVec))
    (i : Fin 3) (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ' : Module.Dual ℂ (ConjModule DownSinglet)),
    Commute (h.barH s φ) (h.bard i s' φ')
```

**`StandardModel.AlgebraRealization.barH_comm_u`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L324).

> The conjugate Higgs symbols commute with the up-type quark symbols: the Higgs is a boson, so
> it carries no statistics against the fermions.

```lean
lemma barH_comm_u : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule HiggsVec))
    (i : Fin 3) (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ' : Module.Dual ℂ UpSinglet),
    Commute (h.barH s φ) (h.u i s' φ')
```

**`StandardModel.AlgebraRealization.barH_comm_baru`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L333).

> The conjugate Higgs symbols commute with the conjugate up-type quark symbols: the Higgs is a
> boson, so it carries no statistics against the fermions.

```lean
lemma barH_comm_baru : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule HiggsVec))
    (i : Fin 3) (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ' : Module.Dual ℂ (ConjModule UpSinglet)),
    Commute (h.barH s φ) (h.baru i s' φ')
```

**`StandardModel.AlgebraRealization.barH_comm_Q`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L342).

> The conjugate Higgs symbols commute with the quark doublet symbols: the Higgs is a boson, so
> it carries no statistics against the fermions.

```lean
lemma barH_comm_Q : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule HiggsVec))
    (i : Fin 3) (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ' : Module.Dual ℂ QuarkDoublet),
    Commute (h.barH s φ) (h.Q i s' φ')
```

**`StandardModel.AlgebraRealization.barH_comm_barQ`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L351).

> The conjugate Higgs symbols commute with the conjugate quark doublet symbols: the Higgs is a
> boson, so it carries no statistics against the fermions.

```lean
lemma barH_comm_barQ : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule HiggsVec))
    (i : Fin 3) (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ' : Module.Dual ℂ (ConjModule QuarkDoublet)),
    Commute (h.barH s φ) (h.barQ i s' φ')
```

**`StandardModel.AlgebraRealization.barH_comm_L`**, a lemma, [line 360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L360).

> The conjugate Higgs symbols commute with the lepton doublet symbols: the Higgs is a boson, so
> it carries no statistics against the fermions.

```lean
lemma barH_comm_L : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule HiggsVec))
    (i : Fin 3) (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ' : Module.Dual ℂ LeptonDoubletV),
    Commute (h.barH s φ) (h.L i s' φ')
```

**`StandardModel.AlgebraRealization.barH_comm_barL`**, a lemma, [line 369](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L369).

> The conjugate Higgs symbols commute with the conjugate lepton doublet symbols: the Higgs is a
> boson, so it carries no statistics against the fermions.

```lean
lemma barH_comm_barL : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule HiggsVec))
    (i : Fin 3) (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ' : Module.Dual ℂ (ConjModule LeptonDoubletV)),
    Commute (h.barH s φ) (h.barL i s' φ')
```

**`StandardModel.AlgebraRealization.barH_comm_e`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L379).

> The conjugate Higgs symbols commute with the lepton singlet symbols: the Higgs is a boson, so
> it carries no statistics against the fermions.

```lean
lemma barH_comm_e : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule HiggsVec))
    (i : Fin 3) (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ' : Module.Dual ℂ LeptonSinglet),
    Commute (h.barH s φ) (h.e i s' φ')
```

**`StandardModel.AlgebraRealization.barH_comm_bare`**, a lemma, [line 388](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L388).

> The conjugate Higgs symbols commute with the conjugate lepton singlet symbols: the Higgs is a
> boson, so it carries no statistics against the fermions.

```lean
lemma barH_comm_bare : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule HiggsVec))
    (i : Fin 3) (s' : Multiset (Fin 1 ⊕ Fin 3)) (φ' : Module.Dual ℂ (ConjModule LeptonSinglet)),
    Commute (h.barH s φ) (h.bare i s' φ')
```

**`StandardModel.AlgebraRealization.d_anticomm_d`**, a lemma, [line 397](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L397).

> The down-type quark symbols anticommute among themselves.

```lean
lemma d_anticomm_d : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ φ' : Module.Dual ℂ DownSinglet),
    h.d i s φ * h.d j s' φ' = -(h.d j s' φ' * h.d i s φ)
```

**`StandardModel.AlgebraRealization.d_anticomm_bard`**, a lemma, [line 405](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L405).

> The down-type quark symbols anticommute with the conjugate down-type quark symbols.

```lean
lemma d_anticomm_bard : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ DownSinglet) (φ' : Module.Dual ℂ (ConjModule DownSinglet)),
    h.d i s φ * h.bard j s' φ' = -(h.bard j s' φ' * h.d i s φ)
```

**`StandardModel.AlgebraRealization.d_anticomm_u`**, a lemma, [line 413](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L413).

> The down-type quark symbols anticommute with the up-type quark symbols.

```lean
lemma d_anticomm_u : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ DownSinglet)
    (φ' : Module.Dual ℂ UpSinglet),
    h.d i s φ * h.u j s' φ' = -(h.u j s' φ' * h.d i s φ)
```

**`StandardModel.AlgebraRealization.d_anticomm_baru`**, a lemma, [line 422](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L422).

> The down-type quark symbols anticommute with the conjugate up-type quark symbols.

```lean
lemma d_anticomm_baru : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ DownSinglet) (φ' : Module.Dual ℂ (ConjModule UpSinglet)),
    h.d i s φ * h.baru j s' φ' = -(h.baru j s' φ' * h.d i s φ)
```

**`StandardModel.AlgebraRealization.d_anticomm_Q`**, a lemma, [line 430](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L430).

> The down-type quark symbols anticommute with the quark doublet symbols.

```lean
lemma d_anticomm_Q : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ DownSinglet)
    (φ' : Module.Dual ℂ QuarkDoublet),
    h.d i s φ * h.Q j s' φ' = -(h.Q j s' φ' * h.d i s φ)
```

**`StandardModel.AlgebraRealization.d_anticomm_barQ`**, a lemma, [line 439](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L439).

> The down-type quark symbols anticommute with the conjugate quark doublet symbols.

```lean
lemma d_anticomm_barQ : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ DownSinglet) (φ' : Module.Dual ℂ (ConjModule QuarkDoublet)),
    h.d i s φ * h.barQ j s' φ' = -(h.barQ j s' φ' * h.d i s φ)
```

**`StandardModel.AlgebraRealization.d_anticomm_L`**, a lemma, [line 447](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L447).

> The down-type quark symbols anticommute with the lepton doublet symbols.

```lean
lemma d_anticomm_L : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ DownSinglet)
    (φ' : Module.Dual ℂ LeptonDoubletV),
    h.d i s φ * h.L j s' φ' = -(h.L j s' φ' * h.d i s φ)
```

**`StandardModel.AlgebraRealization.d_anticomm_barL`**, a lemma, [line 456](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L456).

> The down-type quark symbols anticommute with the conjugate lepton doublet symbols.

```lean
lemma d_anticomm_barL : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ DownSinglet) (φ' : Module.Dual ℂ (ConjModule LeptonDoubletV)),
    h.d i s φ * h.barL j s' φ' = -(h.barL j s' φ' * h.d i s φ)
```

**`StandardModel.AlgebraRealization.d_anticomm_e`**, a lemma, [line 464](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L464).

> The down-type quark symbols anticommute with the lepton singlet symbols.

```lean
lemma d_anticomm_e : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ DownSinglet)
    (φ' : Module.Dual ℂ LeptonSinglet),
    h.d i s φ * h.e j s' φ' = -(h.e j s' φ' * h.d i s φ)
```

**`StandardModel.AlgebraRealization.d_anticomm_bare`**, a lemma, [line 473](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L473).

> The down-type quark symbols anticommute with the conjugate lepton singlet symbols.

```lean
lemma d_anticomm_bare : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ DownSinglet) (φ' : Module.Dual ℂ (ConjModule LeptonSinglet)),
    h.d i s φ * h.bare j s' φ' = -(h.bare j s' φ' * h.d i s φ)
```

**`StandardModel.AlgebraRealization.bard_anticomm_bard`**, a lemma, [line 481](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L481).

> The conjugate down-type quark symbols anticommute among themselves.

```lean
lemma bard_anticomm_bard : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ φ' : Module.Dual ℂ (ConjModule DownSinglet)),
    h.bard i s φ * h.bard j s' φ' = -(h.bard j s' φ' * h.bard i s φ)
```

**`StandardModel.AlgebraRealization.bard_anticomm_u`**, a lemma, [line 489](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L489).

> The conjugate down-type quark symbols anticommute with the up-type quark symbols.

```lean
lemma bard_anticomm_u : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule DownSinglet)) (φ' : Module.Dual ℂ UpSinglet),
    h.bard i s φ * h.u j s' φ' = -(h.u j s' φ' * h.bard i s φ)
```

**`StandardModel.AlgebraRealization.bard_anticomm_baru`**, a lemma, [line 497](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L497).

> The conjugate down-type quark symbols anticommute with the conjugate up-type quark symbols.

```lean
lemma bard_anticomm_baru : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule DownSinglet)) (φ' : Module.Dual ℂ (ConjModule UpSinglet)),
    h.bard i s φ * h.baru j s' φ' = -(h.baru j s' φ' * h.bard i s φ)
```

**`StandardModel.AlgebraRealization.bard_anticomm_Q`**, a lemma, [line 505](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L505).

> The conjugate down-type quark symbols anticommute with the quark doublet symbols.

```lean
lemma bard_anticomm_Q : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule DownSinglet)) (φ' : Module.Dual ℂ QuarkDoublet),
    h.bard i s φ * h.Q j s' φ' = -(h.Q j s' φ' * h.bard i s φ)
```

**`StandardModel.AlgebraRealization.bard_anticomm_barQ`**, a lemma, [line 513](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L513).

> The conjugate down-type quark symbols anticommute with the conjugate quark doublet symbols.

```lean
lemma bard_anticomm_barQ : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule DownSinglet)) (φ' : Module.Dual ℂ (ConjModule QuarkDoublet)),
    h.bard i s φ * h.barQ j s' φ' = -(h.barQ j s' φ' * h.bard i s φ)
```

**`StandardModel.AlgebraRealization.bard_anticomm_L`**, a lemma, [line 521](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L521).

> The conjugate down-type quark symbols anticommute with the lepton doublet symbols.

```lean
lemma bard_anticomm_L : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule DownSinglet)) (φ' : Module.Dual ℂ LeptonDoubletV),
    h.bard i s φ * h.L j s' φ' = -(h.L j s' φ' * h.bard i s φ)
```

**`StandardModel.AlgebraRealization.bard_anticomm_barL`**, a lemma, [line 530](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L530).

> The conjugate down-type quark symbols anticommute with the conjugate lepton doublet symbols.

```lean
lemma bard_anticomm_barL : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule DownSinglet)) (φ' : Module.Dual ℂ (ConjModule LeptonDoubletV)),
    h.bard i s φ * h.barL j s' φ' = -(h.barL j s' φ' * h.bard i s φ)
```

**`StandardModel.AlgebraRealization.bard_anticomm_e`**, a lemma, [line 538](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L538).

> The conjugate down-type quark symbols anticommute with the lepton singlet symbols.

```lean
lemma bard_anticomm_e : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule DownSinglet)) (φ' : Module.Dual ℂ LeptonSinglet),
    h.bard i s φ * h.e j s' φ' = -(h.e j s' φ' * h.bard i s φ)
```

**`StandardModel.AlgebraRealization.bard_anticomm_bare`**, a lemma, [line 547](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L547).

> The conjugate down-type quark symbols anticommute with the conjugate lepton singlet symbols.

```lean
lemma bard_anticomm_bare : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule DownSinglet)) (φ' : Module.Dual ℂ (ConjModule LeptonSinglet)),
    h.bard i s φ * h.bare j s' φ' = -(h.bare j s' φ' * h.bard i s φ)
```

**`StandardModel.AlgebraRealization.u_anticomm_u`**, a lemma, [line 555](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L555).

> The up-type quark symbols anticommute among themselves.

```lean
lemma u_anticomm_u : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ φ' : Module.Dual ℂ UpSinglet),
    h.u i s φ * h.u j s' φ' = -(h.u j s' φ' * h.u i s φ)
```

**`StandardModel.AlgebraRealization.u_anticomm_baru`**, a lemma, [line 563](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L563).

> The up-type quark symbols anticommute with the conjugate up-type quark symbols.

```lean
lemma u_anticomm_baru : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ UpSinglet)
    (φ' : Module.Dual ℂ (ConjModule UpSinglet)),
    h.u i s φ * h.baru j s' φ' = -(h.baru j s' φ' * h.u i s φ)
```

**`StandardModel.AlgebraRealization.u_anticomm_Q`**, a lemma, [line 572](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L572).

> The up-type quark symbols anticommute with the quark doublet symbols.

```lean
lemma u_anticomm_Q : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ UpSinglet)
    (φ' : Module.Dual ℂ QuarkDoublet),
    h.u i s φ * h.Q j s' φ' = -(h.Q j s' φ' * h.u i s φ)
```

**`StandardModel.AlgebraRealization.u_anticomm_barQ`**, a lemma, [line 580](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L580).

> The up-type quark symbols anticommute with the conjugate quark doublet symbols.

```lean
lemma u_anticomm_barQ : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ UpSinglet)
    (φ' : Module.Dual ℂ (ConjModule QuarkDoublet)),
    h.u i s φ * h.barQ j s' φ' = -(h.barQ j s' φ' * h.u i s φ)
```

**`StandardModel.AlgebraRealization.u_anticomm_L`**, a lemma, [line 589](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L589).

> The up-type quark symbols anticommute with the lepton doublet symbols.

```lean
lemma u_anticomm_L : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ UpSinglet)
    (φ' : Module.Dual ℂ LeptonDoubletV),
    h.u i s φ * h.L j s' φ' = -(h.L j s' φ' * h.u i s φ)
```

**`StandardModel.AlgebraRealization.u_anticomm_barL`**, a lemma, [line 597](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L597).

> The up-type quark symbols anticommute with the conjugate lepton doublet symbols.

```lean
lemma u_anticomm_barL : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ UpSinglet)
    (φ' : Module.Dual ℂ (ConjModule LeptonDoubletV)),
    h.u i s φ * h.barL j s' φ' = -(h.barL j s' φ' * h.u i s φ)
```

**`StandardModel.AlgebraRealization.u_anticomm_e`**, a lemma, [line 606](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L606).

> The up-type quark symbols anticommute with the lepton singlet symbols.

```lean
lemma u_anticomm_e : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ UpSinglet)
    (φ' : Module.Dual ℂ LeptonSinglet),
    h.u i s φ * h.e j s' φ' = -(h.e j s' φ' * h.u i s φ)
```

**`StandardModel.AlgebraRealization.u_anticomm_bare`**, a lemma, [line 614](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L614).

> The up-type quark symbols anticommute with the conjugate lepton singlet symbols.

```lean
lemma u_anticomm_bare : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ UpSinglet)
    (φ' : Module.Dual ℂ (ConjModule LeptonSinglet)),
    h.u i s φ * h.bare j s' φ' = -(h.bare j s' φ' * h.u i s φ)
```

**`StandardModel.AlgebraRealization.baru_anticomm_baru`**, a lemma, [line 623](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L623).

> The conjugate up-type quark symbols anticommute among themselves.

```lean
lemma baru_anticomm_baru : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ φ' : Module.Dual ℂ (ConjModule UpSinglet)),
    h.baru i s φ * h.baru j s' φ' = -(h.baru j s' φ' * h.baru i s φ)
```

**`StandardModel.AlgebraRealization.baru_anticomm_Q`**, a lemma, [line 631](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L631).

> The conjugate up-type quark symbols anticommute with the quark doublet symbols.

```lean
lemma baru_anticomm_Q : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule UpSinglet)) (φ' : Module.Dual ℂ QuarkDoublet),
    h.baru i s φ * h.Q j s' φ' = -(h.Q j s' φ' * h.baru i s φ)
```

**`StandardModel.AlgebraRealization.baru_anticomm_barQ`**, a lemma, [line 639](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L639).

> The conjugate up-type quark symbols anticommute with the conjugate quark doublet symbols.

```lean
lemma baru_anticomm_barQ : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule UpSinglet)) (φ' : Module.Dual ℂ (ConjModule QuarkDoublet)),
    h.baru i s φ * h.barQ j s' φ' = -(h.barQ j s' φ' * h.baru i s φ)
```

**`StandardModel.AlgebraRealization.baru_anticomm_L`**, a lemma, [line 647](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L647).

> The conjugate up-type quark symbols anticommute with the lepton doublet symbols.

```lean
lemma baru_anticomm_L : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule UpSinglet)) (φ' : Module.Dual ℂ LeptonDoubletV),
    h.baru i s φ * h.L j s' φ' = -(h.L j s' φ' * h.baru i s φ)
```

**`StandardModel.AlgebraRealization.baru_anticomm_barL`**, a lemma, [line 655](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L655).

> The conjugate up-type quark symbols anticommute with the conjugate lepton doublet symbols.

```lean
lemma baru_anticomm_barL : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule UpSinglet)) (φ' : Module.Dual ℂ (ConjModule LeptonDoubletV)),
    h.baru i s φ * h.barL j s' φ' = -(h.barL j s' φ' * h.baru i s φ)
```

**`StandardModel.AlgebraRealization.baru_anticomm_e`**, a lemma, [line 663](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L663).

> The conjugate up-type quark symbols anticommute with the lepton singlet symbols.

```lean
lemma baru_anticomm_e : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule UpSinglet)) (φ' : Module.Dual ℂ LeptonSinglet),
    h.baru i s φ * h.e j s' φ' = -(h.e j s' φ' * h.baru i s φ)
```

**`StandardModel.AlgebraRealization.baru_anticomm_bare`**, a lemma, [line 671](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L671).

> The conjugate up-type quark symbols anticommute with the conjugate lepton singlet symbols.

```lean
lemma baru_anticomm_bare : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule UpSinglet)) (φ' : Module.Dual ℂ (ConjModule LeptonSinglet)),
    h.baru i s φ * h.bare j s' φ' = -(h.bare j s' φ' * h.baru i s φ)
```

**`StandardModel.AlgebraRealization.Q_anticomm_Q`**, a lemma, [line 679](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L679).

> The quark doublet symbols anticommute among themselves.

```lean
lemma Q_anticomm_Q : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ φ' : Module.Dual ℂ QuarkDoublet),
    h.Q i s φ * h.Q j s' φ' = -(h.Q j s' φ' * h.Q i s φ)
```

**`StandardModel.AlgebraRealization.Q_anticomm_barQ`**, a lemma, [line 687](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L687).

> The quark doublet symbols anticommute with the conjugate quark doublet symbols.

```lean
lemma Q_anticomm_barQ : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ QuarkDoublet) (φ' : Module.Dual ℂ (ConjModule QuarkDoublet)),
    h.Q i s φ * h.barQ j s' φ' = -(h.barQ j s' φ' * h.Q i s φ)
```

**`StandardModel.AlgebraRealization.Q_anticomm_L`**, a lemma, [line 695](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L695).

> The quark doublet symbols anticommute with the lepton doublet symbols.

```lean
lemma Q_anticomm_L : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ QuarkDoublet)
    (φ' : Module.Dual ℂ LeptonDoubletV),
    h.Q i s φ * h.L j s' φ' = -(h.L j s' φ' * h.Q i s φ)
```

**`StandardModel.AlgebraRealization.Q_anticomm_barL`**, a lemma, [line 704](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L704).

> The quark doublet symbols anticommute with the conjugate lepton doublet symbols.

```lean
lemma Q_anticomm_barL : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ QuarkDoublet) (φ' : Module.Dual ℂ (ConjModule LeptonDoubletV)),
    h.Q i s φ * h.barL j s' φ' = -(h.barL j s' φ' * h.Q i s φ)
```

**`StandardModel.AlgebraRealization.Q_anticomm_e`**, a lemma, [line 712](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L712).

> The quark doublet symbols anticommute with the lepton singlet symbols.

```lean
lemma Q_anticomm_e : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ QuarkDoublet)
    (φ' : Module.Dual ℂ LeptonSinglet),
    h.Q i s φ * h.e j s' φ' = -(h.e j s' φ' * h.Q i s φ)
```

**`StandardModel.AlgebraRealization.Q_anticomm_bare`**, a lemma, [line 721](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L721).

> The quark doublet symbols anticommute with the conjugate lepton singlet symbols.

```lean
lemma Q_anticomm_bare : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ QuarkDoublet) (φ' : Module.Dual ℂ (ConjModule LeptonSinglet)),
    h.Q i s φ * h.bare j s' φ' = -(h.bare j s' φ' * h.Q i s φ)
```

**`StandardModel.AlgebraRealization.barQ_anticomm_barQ`**, a lemma, [line 729](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L729).

> The conjugate quark doublet symbols anticommute among themselves.

```lean
lemma barQ_anticomm_barQ : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ φ' : Module.Dual ℂ (ConjModule QuarkDoublet)),
    h.barQ i s φ * h.barQ j s' φ' = -(h.barQ j s' φ' * h.barQ i s φ)
```

**`StandardModel.AlgebraRealization.barQ_anticomm_L`**, a lemma, [line 737](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L737).

> The conjugate quark doublet symbols anticommute with the lepton doublet symbols.

```lean
lemma barQ_anticomm_L : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule QuarkDoublet)) (φ' : Module.Dual ℂ LeptonDoubletV),
    h.barQ i s φ * h.L j s' φ' = -(h.L j s' φ' * h.barQ i s φ)
```

**`StandardModel.AlgebraRealization.barQ_anticomm_barL`**, a lemma, [line 745](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L745).

> The conjugate quark doublet symbols anticommute with the conjugate lepton doublet symbols.

```lean
lemma barQ_anticomm_barL : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule QuarkDoublet)) (φ' : Module.Dual ℂ (ConjModule LeptonDoubletV)),
    h.barQ i s φ * h.barL j s' φ' = -(h.barL j s' φ' * h.barQ i s φ)
```

**`StandardModel.AlgebraRealization.barQ_anticomm_e`**, a lemma, [line 753](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L753).

> The conjugate quark doublet symbols anticommute with the lepton singlet symbols.

```lean
lemma barQ_anticomm_e : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule QuarkDoublet)) (φ' : Module.Dual ℂ LeptonSinglet),
    h.barQ i s φ * h.e j s' φ' = -(h.e j s' φ' * h.barQ i s φ)
```

**`StandardModel.AlgebraRealization.barQ_anticomm_bare`**, a lemma, [line 761](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L761).

> The conjugate quark doublet symbols anticommute with the conjugate lepton singlet symbols.

```lean
lemma barQ_anticomm_bare : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule QuarkDoublet)) (φ' : Module.Dual ℂ (ConjModule LeptonSinglet)),
    h.barQ i s φ * h.bare j s' φ' = -(h.bare j s' φ' * h.barQ i s φ)
```

**`StandardModel.AlgebraRealization.L_anticomm_L`**, a lemma, [line 769](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L769).

> The lepton doublet symbols anticommute among themselves.

```lean
lemma L_anticomm_L : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ φ' : Module.Dual ℂ LeptonDoubletV),
    h.L i s φ * h.L j s' φ' = -(h.L j s' φ' * h.L i s φ)
```

**`StandardModel.AlgebraRealization.L_anticomm_barL`**, a lemma, [line 777](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L777).

> The lepton doublet symbols anticommute with the conjugate lepton doublet symbols.

```lean
lemma L_anticomm_barL : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ LeptonDoubletV) (φ' : Module.Dual ℂ (ConjModule LeptonDoubletV)),
    h.L i s φ * h.barL j s' φ' = -(h.barL j s' φ' * h.L i s φ)
```

**`StandardModel.AlgebraRealization.L_anticomm_e`**, a lemma, [line 785](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L785).

> The lepton doublet symbols anticommute with the lepton singlet symbols.

```lean
lemma L_anticomm_e : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ LeptonDoubletV)
    (φ' : Module.Dual ℂ LeptonSinglet),
    h.L i s φ * h.e j s' φ' = -(h.e j s' φ' * h.L i s φ)
```

**`StandardModel.AlgebraRealization.L_anticomm_bare`**, a lemma, [line 794](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L794).

> The lepton doublet symbols anticommute with the conjugate lepton singlet symbols.

```lean
lemma L_anticomm_bare : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ LeptonDoubletV) (φ' : Module.Dual ℂ (ConjModule LeptonSinglet)),
    h.L i s φ * h.bare j s' φ' = -(h.bare j s' φ' * h.L i s φ)
```

**`StandardModel.AlgebraRealization.barL_anticomm_barL`**, a lemma, [line 802](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L802).

> The conjugate lepton doublet symbols anticommute among themselves.

```lean
lemma barL_anticomm_barL : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ φ' : Module.Dual ℂ (ConjModule LeptonDoubletV)),
    h.barL i s φ * h.barL j s' φ' = -(h.barL j s' φ' * h.barL i s φ)
```

**`StandardModel.AlgebraRealization.barL_anticomm_e`**, a lemma, [line 810](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L810).

> The conjugate lepton doublet symbols anticommute with the lepton singlet symbols.

```lean
lemma barL_anticomm_e : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule LeptonDoubletV)) (φ' : Module.Dual ℂ LeptonSinglet),
    h.barL i s φ * h.e j s' φ' = -(h.e j s' φ' * h.barL i s φ)
```

**`StandardModel.AlgebraRealization.barL_anticomm_bare`**, a lemma, [line 818](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L818).

> The conjugate lepton doublet symbols anticommute with the conjugate lepton singlet symbols.

```lean
lemma barL_anticomm_bare : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule LeptonDoubletV)) (φ' : Module.Dual ℂ (ConjModule LeptonSinglet))
      ,
    h.barL i s φ * h.bare j s' φ' = -(h.bare j s' φ' * h.barL i s φ)
```

**`StandardModel.AlgebraRealization.e_anticomm_e`**, a lemma, [line 827](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L827).

> The lepton singlet symbols anticommute among themselves.

```lean
lemma e_anticomm_e : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ φ' : Module.Dual ℂ LeptonSinglet),
    h.e i s φ * h.e j s' φ' = -(h.e j s' φ' * h.e i s φ)
```

**`StandardModel.AlgebraRealization.e_anticomm_bare`**, a lemma, [line 835](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L835).

> The lepton singlet symbols anticommute with the conjugate lepton singlet symbols.

```lean
lemma e_anticomm_bare : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ LeptonSinglet) (φ' : Module.Dual ℂ (ConjModule LeptonSinglet)),
    h.e i s φ * h.bare j s' φ' = -(h.bare j s' φ' * h.e i s φ)
```

**`StandardModel.AlgebraRealization.bare_anticomm_bare`**, a lemma, [line 843](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean#L843).

> The conjugate lepton singlet symbols anticommute among themselves.

```lean
lemma bare_anticomm_bare : ∀ (i j : Fin 3) (s s' : Multiset (Fin 1 ⊕ Fin 3))
    (φ φ' : Module.Dual ℂ (ConjModule LeptonSinglet)),
    h.bare i s φ * h.bare j s' φ' = -(h.bare j s' φ' * h.bare i s φ)
```

## Depends on

- [The algebra valued Standard model](realization-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/Commutations.lean)
