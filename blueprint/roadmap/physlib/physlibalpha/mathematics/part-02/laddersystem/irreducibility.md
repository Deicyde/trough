---
declaration: module
origin: cited
lean: LadderSystem.vacuumSpan_eq_of_ne_bot, LadderSystem.moveOneTo, LadderSystem.countWord_moveOneTo_perm, LadderSystem.E_word_countWord, LadderSystem.mapsTo_aeval, LadderSystem.exists_word_countWord_mem_of_ne_bot, LadderSystem.sum_eq_length_countWord, LadderSystem.sum_moveOneTo
statement: formalized
proof: formalized
---

# Irreducibility of the excitation-number sector

The module `PhyslibAlpha.Mathematics.LadderSystem.Irreducibility`, [PhyslibAlpha/Mathematics/LadderSystem/Irreducibility.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Irreducibility.lean): 14 declarations, 13 with a docstring, 1 listed as significant.

> The excitation-number sector `vacuumSpan L Ω n` of a ladder system is `gl(d)`-irreducible.

## i. Overview

> `LadderSystem.vacuumSpan L Ω n` is `gl(d)`-irreducible: the only submodules of `vacuumSpan L Ω n`
> invariant under every `E i j` are `⊥` and `vacuumSpan L Ω n` itself. Completeness in an ambient
> Hilbert space is a separate analytic question. The proof uses linear algebra over a field of
> characteristic zero.

## ii. Key results

> - `LadderSystem.vacuumSpan_eq_of_ne_bot` : a nonzero `E i j`-invariant submodule of
>     `vacuumSpan L Ω n` is all of `vacuumSpan L Ω n`.

## iv. References

> * None.

## A. Moving a quantum between modes

**`LadderSystem.moveOneTo`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Irreducibility.lean#L56).

> `α` with one quantum moved from color `j` to color `i`. Only meaningful for `i ≠ j`; the
> degenerate `i = j` case is handled separately by `N_word`.

```lean
def moveOneTo (α : Fin d → ℕ) (i j : Fin d) : Fin d → ℕ
```

**`LadderSystem.countWord_moveOneTo_perm`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Irreducibility.lean#L59).

```lean
lemma countWord_moveOneTo_perm {i j : Fin d} (hij : i ≠ j) {α : Fin d → ℕ} :
    List.Perm (i :: (countWord d α).erase j) (countWord d (moveOneTo α i j))
```

**`LadderSystem.E_word_countWord`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Irreducibility.lean#L81).

> The transfer formula: `E i j` moves one quantum from color `j` to color `i`, scaled by
> `j`'s occupation number.

```lean
lemma E_word_countWord {Ω : V} (P : L.HasVacuum Ω) {i j : Fin d} (hij : i ≠ j)
    {α : Fin d → ℕ} :
    L.E i j (L.word (countWord d α) Ω) =
      (α j : K) • L.word (countWord d (moveOneTo α i j)) Ω
```

## B. Extracting a single basis vector from an invariant submodule

**`LadderSystem.mapsTo_aeval`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Irreducibility.lean#L96).

> A submodule invariant under an endomorphism `M` is invariant under any polynomial in `M`.

```lean
lemma mapsTo_aeval {W : Submodule K V} {M : Module.End K V} (hW : ∀ w ∈ W, M w ∈ W)
    (p : Polynomial K) : ∀ w ∈ W, (Polynomial.aeval M p) w ∈ W
```

**`LadderSystem.exists_word_countWord_mem_of_ne_bot`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Irreducibility.lean#L114).

> A nonzero `E i j`-invariant submodule of `vacuumSpan L Ω n` contains an occupation-number
> basis vector. A Lagrange-interpolation polynomial in the diagonal separator
> `∑ᵢ(n+1)^i • Nᵢ` projects a nonzero element onto one of its basis components.

```lean
lemma exists_word_countWord_mem_of_ne_bot {Ω : V} (P : L.HasVacuum Ω) (n : ℕ)
    {W : Submodule K V} (hWle : W ≤ vacuumSpan L Ω n)
    (hWE : ∀ i j, ∀ w ∈ W, L.E i j w ∈ W) (hWbot : W ≠ ⊥) :
    ∃ α : CountFun d n, L.word (countWord d α.1) Ω ∈ W
```

## C. Connectivity: one basis vector reaches every other

**`LadderSystem.sum_eq_length_countWord`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Irreducibility.lean#L190).

> The total occupation number matches the length of the canonical word representing it.

```lean
lemma sum_eq_length_countWord (α : Fin d → ℕ) : (∑ c, α c) = (countWord d α).length
```

**`LadderSystem.sum_moveOneTo`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Irreducibility.lean#L196).

> Moving one quantum between two modes preserves the total occupation number.

```lean
lemma sum_moveOneTo {i j : Fin d} (hij : i ≠ j) {α : Fin d → ℕ} (hj : α j ≠ 0) :
    (∑ c, moveOneTo α i j c) = ∑ c, α c
```

**`LadderSystem.moveOneTo_self`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Irreducibility.lean#L207).

> `moveOneTo` at the color it moves quanta *into* just increments that color's count.

```lean
lemma moveOneTo_self (α : Fin d → ℕ) (i j : Fin d) : moveOneTo α i j i = α i + 1
```

**`LadderSystem.moveOneTo_moveOneTo`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Irreducibility.lean#L213).

> Moving a quantum from `j` to `i` and then immediately back from `i` to `j` is the identity.

```lean
lemma moveOneTo_moveOneTo {i j : Fin d} (hij : i ≠ j) {α : Fin d → ℕ} (hj : α j ≠ 0) :
    moveOneTo (moveOneTo α i j) j i = α
```

**`LadderSystem.word_countWord_moveOneTo_mem`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Irreducibility.lean#L236).

> The atomic move: if `W` is `E i j`-invariant and contains the word for `β`, and mode `k`
> is occupied, `W` also contains the word obtained by moving one quantum from `k` to any other
> mode `l`.

```lean
lemma word_countWord_moveOneTo_mem {Ω : V} (P : L.HasVacuum Ω) {W : Submodule K V}
    (hWE : ∀ i j, ∀ w ∈ W, L.E i j w ∈ W) {β : Fin d → ℕ}
    (hmem : L.word (countWord d β) Ω ∈ W) {l k : Fin d} (hkl : l ≠ k) (hk : β k ≠ 0) :
    L.word (countWord d (moveOneTo β l k)) Ω ∈ W
```

**`LadderSystem.word_countWord_hub_mem_of_mem`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Irreducibility.lean#L249).

> Every occupation-number word reaches the mode-`0` hub word, given `W`
> is `E i j`-invariant and contains it. Proved by strong induction on the mass sitting outside
> mode `0`.

```lean
lemma word_countWord_hub_mem_of_mem {hd : 0 < d} {Ω : V} (P : L.HasVacuum Ω)
    {W : Submodule K V} (hWE : ∀ i j, ∀ w ∈ W, L.E i j w ∈ W) :
    ∀ m : ℕ, ∀ α : Fin d → ℕ, (∑ c, α c) - α (⟨0, hd⟩ : Fin d) = m →
      L.word (countWord d α) Ω ∈ W →
      L.word (countWord d (fun c => if c = (⟨0, hd⟩ : Fin d) then (∑ c, α c) else 0)) Ω ∈ W
```

**`LadderSystem.word_countWord_mem_of_hub_mem`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Irreducibility.lean#L294).

> The hub word reaches every occupation-number word, given `W` is `E i j`-invariant and
> contains it. Proved by strong induction on the mass sitting outside mode `0` in the target.

```lean
lemma word_countWord_mem_of_hub_mem {hd : 0 < d} {Ω : V} (P : L.HasVacuum Ω)
    {W : Submodule K V} (hWE : ∀ i j, ∀ w ∈ W, L.E i j w ∈ W) :
    ∀ m : ℕ, ∀ α : Fin d → ℕ, (∑ c, α c) - α (⟨0, hd⟩ : Fin d) = m →
      L.word (countWord d (fun c => if c = (⟨0, hd⟩ : Fin d) then (∑ c, α c) else 0)) Ω ∈ W →
      L.word (countWord d α) Ω ∈ W
```

**`LadderSystem.word_countWord_mem_of_mem`**, a lemma, [line 346](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Irreducibility.lean#L346).

> Connectivity: any two occupation-number words of the same total excitation number reach
> each other, given `W` is `E i j`-invariant and contains one of them.

```lean
lemma word_countWord_mem_of_mem {hd : 0 < d} {Ω : V} (P : L.HasVacuum Ω)
    {W : Submodule K V} (hWE : ∀ i j, ∀ w ∈ W, L.E i j w ∈ W) {α α' : Fin d → ℕ}
    (hsum : (∑ c, α c) = ∑ c, α' c) (hmem : L.word (countWord d α) Ω ∈ W) :
    L.word (countWord d α') Ω ∈ W
```

## D. Irreducibility

**`LadderSystem.vacuumSpan_eq_of_ne_bot`**, a theorem, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Irreducibility.lean#L363). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> `vacuumSpan L Ω n` is `gl(d)`-irreducible. The only submodules of `vacuumSpan L Ω n`
> invariant under every `E i j` are `⊥` and `vacuumSpan L Ω n` itself.

```lean
theorem vacuumSpan_eq_of_ne_bot {hd : 0 < d} {Ω : V} (P : L.HasVacuum Ω) (n : ℕ)
    {W : Submodule K V} (hWle : W ≤ vacuumSpan L Ω n)
    (hWE : ∀ i j, ∀ w ∈ W, L.E i j w ∈ W) (hWbot : W ≠ ⊥) :
    W = vacuumSpan L Ω n
```

## Depends on

- [The occupation-number basis](occupationbasis.md)

## Sources

- [PhyslibAlpha/Mathematics/LadderSystem/Irreducibility.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Irreducibility.lean)
