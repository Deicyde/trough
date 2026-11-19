---
catalog: module
lean: Cedar.SymCC.EncoderState, Cedar.SymCC.Encoder.enumId, Cedar.SymCC.Encoder.smtLibMaxCodePoint, Cedar.SymCC.Encoder.encode
statement: formalized
proof: formalized
---

# Encoder

`Cedar.SymCC.Encoder`, in [Cedar/SymCC/Encoder.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Encoder.lean).

> This file defines the Cedar encoder, which translates a list of boolean Terms
> into a list of SMT assertions. Term encoding is trusted.
>
>  We will use the following type representations for primitive types:
>  * `TermType.bool`:     builtin SMT `Bool` type
>  * `TermType.string`:   builtin SMT `String` type
>  * `TermType.bitvec n`: builtin SMT `(_ BitVec n)` type
>
>  We will represent non-primitive types as SMT algebraic datypes:
>  * `TermType.option T`: a parameterized SMT algebraic datatype of the same name,
>    and with the constructors `(some (val T))` and `(none)`. For each constructor
>    argument, SMTLib introduces a corresponding (total) selector function. We
>    will translate `Term.some` nodes in the Term language as applications of the
>    `val` selector function.
>  * `TermType.entity E`: we represent Cedar entities of entity type E as values
>    of the SMT algebraic datatype E with a single constructor, `(E (E_eid String))`.
>    The selector is named `E_eid`, after the entity type, since SMT-LIB requires
>    unique selector and constructor names across all datatypes.
>    Each entity type E gets an uninterpreted function `f: E → Record_E` that maps
>    instances of E to their attributes.  Similarly, each E
>    gets N uninterpreted functions `g₁: E → Set E₁, ..., gₙ: E → Set Eₙ` that map
>    each instance of E to its ancestor sets of the given types, as specified by
>    the `memberOf` relation in the schema.
>  * `TermType.Record (Map Attr TermType)`: we represent each record term type as
>    an SMT algebraic datatype with a single constructor. The order of arguments
>    to the constructor (the attributes) is important, so we fix that to be the
>    lexicographic order on the attribute names of the underlying record type. We
>    use the argument selector functions to translate `record.get` applications.
>    We can't use raw Cedar attribute names for argument names because they may
>    not be valid SMT identifiers. So, we'll keep a mapping from the attribute
>    names to their unique SMT ids. In general, we'll name SMT record types as
>    "R&lt;i>" where &lt;i> is a natural number and attributes within the record as
>    "R&lt;i>a&lt;j>", where &lt;j> is the attribute's position in the constructor argument
>    list.
>
>  Similarly to types and attributes, all uninterpreted functions, variables, and
>  Terms are mapped to their SMT encoding that conforms to the SMTLib syntax. We
>  keep track of these mappings to ensure that each Term construct is translated
>  to its SMT encoding exactly once.  This translation invariant is necessary for
>  correctness in the case of record type declarations, UF names, and variable
>  names; and it is neccessary for compactness in the case of terms. In
>  particular, the resulting SMT encoding will be in A-normal form (ANF): the body
>  of every s-expression in the encoding consists of atomic subterms (identifiers
>  or literals).

`Cedar.SymCC.EncoderState` (structure, [line 76](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Encoder.lean#L76))

```lean
public structure EncoderState where
  terms : Std.TreeMap Term String (compareOfLessAndEq · ·)
  types : Std.TreeMap TermType String (compareOfLessAndEq · ·)
  uufs  : Std.TreeMap UUF String (compareOfLessAndEq · ·)
  enums : Std.TreeMap EntityType (List String) (compareOfLessAndEq · ·)
deriving Repr
```

`Cedar.SymCC.Encoder.enumId` (definition, [line 94](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Encoder.lean#L94))

```lean
public def enumId (E : String) (n : Nat) : String
```

`Cedar.SymCC.Encoder.smtLibMaxCodePoint` (definition, [line 153](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Encoder.lean#L153))

> The maximum Unicode code point supported in SMT-LIB 2.7.
> Also see `num_codes` in cvc5:
> https://github.com/cvc5/cvc5/blob/b78e7ed23348659db52a32765ad181ae0c26bbd5/src/util/string.h#L53

```lean
public def smtLibMaxCodePoint : Nat
```

`Cedar.SymCC.Encoder.encode` (definition, [line 351](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Encoder.lean#L351))

> Once you've generated `Asserts` with one of the functions in Verifier.lean, you
> can use this function to encode them as SMTLib assertions.
>
> To actually solve these SMTLib assertions, you want to combine this `encode`
> action with other `SolverM` actions, such as `Solver.check-sat` at a minimum.
>
> Then you can run any `SolverM` action `act` with `act |>.run solver`, where
> `solver` is a `Solver` instance you can construct using functions in
> Solver.lean.
>
> Note that `encode` itself first resets the solver in order to define datatypes
> etc.

```lean
public def encode (ts : List Term) (εnv : SymEnv) (produceModels : Bool := false) : SolverM EncoderState
```

## Depends on

- [Env](env.md)
- [Solver](solver.md)

## Sources

- [Cedar/SymCC/Encoder.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Encoder.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.SymCC.Encoder.json)
