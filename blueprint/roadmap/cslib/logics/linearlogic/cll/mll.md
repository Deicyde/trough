---
catalog: module
lean: Cslib.Logic.CLL.Proposition.IsMLL, Cslib.Logic.CLL.Proposition.IsMLL.rec, Cslib.Logic.CLL.Proposition.isMLL_dual, Cslib.Logic.CLL.Proposition.Context.IsMLL, Cslib.Logic.CLL.Proposition.Context.isMLL_fill, Cslib.Logic.CLL.Sequent.IsMLL, Cslib.Logic.CLL.Proof.IsMLL, Cslib.Logic.CLL.Proof.IsMLL.rec, Cslib.Logic.CLL.Proof.isMLL_sequent, Cslib.Logic.CLL.Proof.isMLL_cutFree, Cslib.Logic.CLL.MLL.Proof, Cslib.Logic.CLL.MLL, Cslib.Logic.CLL.MLL.Proof.isMLL_sequent, Cslib.Logic.CLL.Proof.cutFreeToMLL
statement: formalized
proof: formalized
---

# Multiplicative Classical Linear Logic (MLL)

`Cslib.Logics.LinearLogic.CLL.MLL`, in [Cslib/Logics/LinearLogic/CLL/MLL.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/MLL.lean), by Fabrizio Montesi.

> Multiplicative classical linear logic, defined as a fragment of classical linear logic by means of
> a predicate (unbundled style) and `Subtype` (bundled style).
>
> This file serves as the reference example of how to define a fragment of an inference system
> through tagging of `InferenceSystem` and `Subtype`, following the next recipe. It is a work in
> progress: the recipe will evolve together with how the Lean and CSLib ecosystems can
> deal with this general problem.
>
> 1. Define predicates for restricting relevant types to the fragment, here `IsMLL` for propositions
> (`CLL.Proposition`) and proofs (`CLL.Proof`). This part lives under the namespace of the original
> system (here `Cslib.Logic.CLL`). Custom recursors can be defined for convenient case analysis that
> automatically discharges irrelevant cases (those not in the fragment).
> 2. Define the inference system in the fragment -- here `MLL.Proof` -- as an abbreviation of
> a subtype. This part lives under the namespace of the fragment (here `Cslib.Logic.CLL.MLL`).
>
> We also call the first part the 'unbundled part' and the second the 'bundled part'.

`Cslib.Logic.CLL.Proposition.IsMLL` (definition, [line 38](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/MLL.lean#L38))

> A proposition is in the multiplicative fragment of CLL.

```lean
def Proposition.IsMLL : Proposition Atom → Prop
```

`Cslib.Logic.CLL.Proposition.IsMLL.rec` (definition, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/MLL.lean#L45))

> Recursor for MLL propositions.

```lean
def Proposition.IsMLL.rec
    {motive : {a : Proposition Atom} → (h : a.IsMLL) → Sort u}
    (atom : ∀ x : Atom, motive (a := .atom x) (by simp))
    (atomDual : ∀ x : Atom, motive (a := .atomDual x) (by simp))
    (one : motive (a := .one) (by simp))
    (bot : motive (a := .bot) (by simp))
    (tensor : ∀ (a b : Proposition Atom) {ha : a.IsMLL} {hb : b.IsMLL},
      motive ha → motive hb → motive (a :=.tensor a b) (by simp [ha,hb]))
    (parr : ∀ (a b : Proposition Atom) {ha : a.IsMLL} {hb : b.IsMLL},
      motive ha → motive hb → motive (a := .parr a b) (by simp [ha,hb]))
    {a : Proposition Atom} (h : a.IsMLL) : motive (a := a) h
```

`Cslib.Logic.CLL.Proposition.isMLL_dual` (theorem, [line 74](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/MLL.lean#L74))

> Duality in MLL stays in MLL.

```lean
theorem Proposition.isMLL_dual {a : Proposition Atom} (ha : a.IsMLL) : a⫠.IsMLL
```

`Cslib.Logic.CLL.Proposition.Context.IsMLL` (definition, [line 79](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/MLL.lean#L79))

> A multiplicative propositional context.

```lean
def Proposition.Context.IsMLL : Context Atom → Prop
```

`Cslib.Logic.CLL.Proposition.Context.isMLL_fill` (theorem, [line 86](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/MLL.lean#L86))

> Filling a multiplicative propositional context with a multiplicative proposition stays in MLL.

```lean
theorem Proposition.Context.isMLL_fill {c : CLL.Proposition.Context Atom} {a : CLL.Proposition Atom}
    (hc : c.IsMLL) : (c.fill a).IsMLL ↔ a.IsMLL
```

`Cslib.Logic.CLL.Sequent.IsMLL` (definition, [line 95](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/MLL.lean#L95))

> A multiplicative sequent.

```lean
def Sequent.IsMLL (Γ : Sequent Atom)
```

`Cslib.Logic.CLL.Proof.IsMLL` (definition, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/MLL.lean#L101))

> A proof is in MLL.

```lean
def Proof.IsMLL {Γ : Sequent Atom} : ⇓Γ → Prop
```

`Cslib.Logic.CLL.Proof.IsMLL.rec` (definition, [line 109](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/MLL.lean#L109))

> Recursor for MLL derivations.

```lean
def Proof.IsMLL.rec
    {motive : {Γ : Sequent Atom} → {p : Proof Γ} → (h : p.IsMLL) → Sort u}
    (ax : ∀ {a : Proposition Atom} {ha : a.IsMLL}, @motive {a, a⫠} .ax (by simp [ha]))
    (one : @motive {Proposition.one} .one (by simp))
    (bot : ∀ {Γ : Sequent Atom} (p : Proof Γ) {hp : p.IsMLL},
      @motive Γ p hp → @motive (.bot ::ₘ Γ) (.bot p) (by simp [hp]))
    (tensor : ∀ {a b : Proposition Atom} {Γ Δ : Sequent Atom}
      (p : Proof (a ::ₘ Γ)) (q : Proof (b ::ₘ Δ)) {hp : p.IsMLL} {hq : q.IsMLL},
      @motive (a ::ₘ Γ) p hp → @motive (b ::ₘ Δ) q hq →
      @motive ((a ⊗ b) ::ₘ (Γ + Δ)) (.tensor p q) (by simp [hp, hq]))
    (parr : ∀ {a b : Proposition Atom} {Γ : Sequent Atom}
      (p : Proof (a ::ₘ b ::ₘ Γ)) {hp : p.IsMLL},
      @motive (a ::ₘ b ::ₘ Γ) p hp → @motive ((a ⅋ b) ::ₘ Γ) (.parr p) (by simp [hp]))
    (cut : ∀ {a : Proposition Atom} {Γ Δ : Sequent Atom}
      (p : Proof (a ::ₘ Γ)) (q : Proof (a⫠ ::ₘ Δ)) {hp : p.IsMLL} {hq : q.IsMLL},
      @motive (a ::ₘ Γ) p hp → @motive (a⫠ ::ₘ Δ) q hq →
      @motive (Γ + Δ) (.cut p q) (by simp [hp, hq]))
    {Γ : Sequent Atom} {p : Proof Γ} (h : p.IsMLL) : @motive Γ p h
```

`Cslib.Logic.CLL.Proof.isMLL_sequent` (theorem, [line 145](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/MLL.lean#L145))

> A proof in the MLL fragment can only prove MLL sequents.

```lean
theorem Proof.isMLL_sequent {Γ : Sequent Atom} {p : ⇓Γ} (h : p.IsMLL) : Γ.IsMLL
```

`Cslib.Logic.CLL.Proof.isMLL_cutFree` (theorem, [line 158](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/MLL.lean#L158))

> If a CLL derivation is cut-free and concludes an MLL sequent, then it is an MLL derivation.

```lean
theorem Proof.isMLL_cutFree {Γ : Sequent Atom} (p : ⇓Γ) (hΓ : Γ.IsMLL)
    (hp : p.cutFree) : p.IsMLL
```

`Cslib.Logic.CLL.MLL.Proof` (abbreviation, [line 179](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/MLL.lean#L179))

> MLL derivations.

```lean
abbrev MLL.Proof (Γ : CLL.Sequent Atom)
```

`Cslib.Logic.CLL.MLL` (opaque constant, [line 182](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/MLL.lean#L182))

> Tag for the MLL inference system.

```lean
opaque MLL : Type
```

`Cslib.Logic.CLL.MLL.Proof.isMLL_sequent` (theorem, [line 192](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/MLL.lean#L192))

> MLL proofs derive only MLL sequents.

```lean
theorem Proof.isMLL_sequent {Γ : Sequent Atom} (p : MLL⇓Γ) : Γ.IsMLL
```

`Cslib.Logic.CLL.Proof.cutFreeToMLL` (definition, [line 198](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/MLL.lean#L198))

> Downcasting of cut-free CLL proofs of multiplicative sequents into MLL proofs.

```lean
def Proof.cutFreeToMLL {Γ : Sequent Atom} (p : ⇓Γ) (hΓ : Γ.IsMLL) (hp : p.cutFree) : MLL⇓Γ
```

## Depends on

- [Classical Linear Logic](basic.md)

## Sources

- [Cslib/Logics/LinearLogic/CLL/MLL.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/MLL.lean)
