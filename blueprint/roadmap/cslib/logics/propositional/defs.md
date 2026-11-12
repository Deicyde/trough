---
catalog: module
lean: Cslib.Logic.PL.Proposition, Cslib.Logic.PL.instBotProposition, Cslib.Logic.PL.Proposition.neg, Cslib.Logic.PL.Proposition.verum, Cslib.Logic.PL.instTopProposition, Cslib.Logic.PL.Proposition.not_eq, Cslib.Logic.PL.Proposition.subst, Cslib.Logic.PL.IPL, Cslib.Logic.PL.CPL, Cslib.Logic.PL.dne_mem_cpl, Cslib.Logic.PL.LEM, Cslib.Logic.PL.mem_lem, Cslib.Logic.PL.Peirce, Cslib.Logic.PL.mem_peirce
statement: formalized
proof: formalized
---

# Propositions and theories

`Cslib.Logics.Propositional.Defs`, in [Cslib/Logics/Propositional/Defs.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/Defs.lean), by Thomas Waring.

> ## Main definitions
>
> - `Proposition` : the type of propositions over a given type of atom.
> - `IsIntuitionistic` : an inference system on `Proposition Atom` is intuitionistic if it
> derives the principle of explosion.
> - `IsClassical` : an inference is classical if it derives double negation elimination.
> - `Proposition.subst` : replace `atom x` in a `A : Proposition Atom` with `f x`, for a function
>   `f : Atom → Proposition Atom'`. This induces a monad structure on `Proposition`, with
>   `pure := Proposition.atom`.
>
> ## Notation
>
> We instantiate the notation classes `HasAnd`, `HasOr`, `HasImpl`, `HasNot`, `Bot` and `Top` for
> `Proposition Atom` to give access to, respectively, the notations `∧, ∨, →`, `¬`, `⊥` and `⊤` for
> propositional connectives.
>
> ## References
>
> * [J. Avigad, *Mathematical Logic and Computation*][Avigad2022]

`Cslib.Logic.PL.Proposition` (inductive type, [line 46](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/Defs.lean#L46))

> Propositions.

```lean
inductive Proposition (Atom : Type u) : Type u where
  /-- Propositional atoms -/
  | atom (x : Atom)
  /-- Falsum. -/
  | falsum
  /-- Conjunction -/
  | and (a b : Proposition Atom)
  /-- Disjunction -/
  | or (a b : Proposition Atom)
  /-- Implication -/
  | imp (a b : Proposition Atom)
deriving DecidableEq
```

`Cslib.Logic.PL.instBotProposition` (instance, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/Defs.lean#L59))

```lean
instance instBotProposition : Bot (Proposition Atom)
```

`Cslib.Logic.PL.Proposition.neg` (abbreviation, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/Defs.lean#L61))

> We view negation as a defined connective ¬A := A → ⊥

```lean
abbrev Proposition.neg : Proposition Atom → Proposition Atom
```

`Cslib.Logic.PL.Proposition.verum` (abbreviation, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/Defs.lean#L64))

> A fixed choice of a derivable proposition (of course any two are equivalent).

```lean
abbrev Proposition.verum : Proposition Atom
```

`Cslib.Logic.PL.instTopProposition` (instance, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/Defs.lean#L66))

```lean
instance instTopProposition : Top (Proposition Atom)
```

`Cslib.Logic.PL.Proposition.not_eq` (lemma, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/Defs.lean#L76))

```lean
lemma Proposition.not_eq (A : Proposition Atom) : (A → ⊥) = ¬ A
```

`Cslib.Logic.PL.Proposition.subst` (definition, [line 80](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/Defs.lean#L80))

> Substitute each atom in a proposition for a proposition, possibly changing the atomic
> language.

```lean
def Proposition.subst {Atom Atom' : Type*} (f : Atom → Proposition Atom') :
    Proposition Atom → Proposition Atom'
```

`Cslib.Logic.PL.IPL` (abbreviation, [line 94](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/Defs.lean#L94))

> The empty collection of axioms corresponds to intuitionistic propositional logic.

```lean
abbrev IPL (Atom : Type u) : Set (Proposition Atom)
```

`Cslib.Logic.PL.CPL` (abbreviation, [line 97](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/Defs.lean#L97))

> Classical logic adds double negation elimination.

```lean
abbrev CPL (Atom : Type u) : Set (Proposition Atom)
```

`Cslib.Logic.PL.dne_mem_cpl` (lemma, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/Defs.lean#L101))

```lean
lemma dne_mem_cpl (A : Proposition Atom) : (¬¬A → A) ∈ CPL Atom
```

`Cslib.Logic.PL.LEM` (definition, [line 104](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/Defs.lean#L104))

> The axiom system consisting of instances of LEM.

```lean
def LEM (Atom : Type u) : Set (Proposition Atom)
```

`Cslib.Logic.PL.mem_lem` (lemma, [line 108](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/Defs.lean#L108))

```lean
lemma mem_lem (A : Proposition Atom) : (A ∨ ¬ A) ∈ LEM Atom
```

`Cslib.Logic.PL.Peirce` (definition, [line 111](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/Defs.lean#L111))

> The axiom system consisting of instances of Peirce's law.

```lean
def Peirce (Atom : Type u) : Set (Proposition Atom)
```

`Cslib.Logic.PL.mem_peirce` (lemma, [line 116](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/Defs.lean#L116))

```lean
lemma mem_peirce (A B : Proposition Atom) : (((A → B) → A) → A) ∈ Peirce Atom
```

## Depends on

- [Logical operators](../../foundations/logic/operators.md)

## Sources

- [Cslib/Logics/Propositional/Defs.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/Defs.lean)
