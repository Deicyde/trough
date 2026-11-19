---
catalog: module
lean: Cedar.SymCC.UUF, Cedar.SymCC.ExtOp, Cedar.SymCC.Op, Cedar.SymCC.UUF.lt, Cedar.SymCC.UUF.decLt, Cedar.SymCC.ExtOp.lt, Cedar.SymCC.ExtOp.decLt, Cedar.SymCC.Op.mkName, Cedar.SymCC.Op.lt, Cedar.SymCC.Op.decLt
statement: formalized
proof: formalized
---

# Op

`Cedar.SymCC.Op`, in [Cedar/SymCC/Op.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Op.lean).

> This file defines the operators on Cedar Terms. See `Term.lean` for the
> definition of the Term language.
>
> There are three kinds of term operators:
> 1. Operators that map directly to an underlying SMT theory
> 2. Operators for constructing and destructing core ADTs that are lowered to SMT
>    by a trusted code generation pass. This also includes core operators whose
>    semantics we don't model in the Term language (but rather directly in SMT),
>    such as `like`.
> 3. Operators for destructing extension ADTs, also lowered by the trusted pass.
>
> We separate extension operators into their own ADT (`ExtOp`) to make it easier
> to add more such operators in the future in a way that's fairly independent of
> the other operators.
>
> We embed SMT and core ADT operators directly into the top-level `Op` ADT, to
> simplify pattern matching against them within rewrite rules.

`Cedar.SymCC.UUF` (structure, [line 45](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Op.lean#L45))

```lean
public structure UUF where         -- uninterpreted unary function
  id : String
  arg : TermType
  out : TermType
```

`Cedar.SymCC.ExtOp` (inductive type, [line 50](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Op.lean#L50))

```lean
public inductive ExtOp : Type where -- extension ADT operators
  | decimal.val
  | ipaddr.isV4
  | ipaddr.addrV4
  | ipaddr.prefixV4
  | ipaddr.addrV6
  | ipaddr.prefixV6
  | datetime.val
  | datetime.ofBitVec
  | duration.val
  | duration.ofBitVec
```

`Cedar.SymCC.Op` (inductive type, [line 62](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Op.lean#L62))

```lean
public inductive Op : Type where
  ---------- SMTLib core theory of equality with uninterpreted functions (`UF`) ----------
  | not
  | and
  | or
  | eq
  | ite
  | uuf : UUF → Op
  ---------- SMTLib theory of finite bitvectors (`BV`) ----------
  | bvneg
  | bvadd
  | bvsub
  | bvmul
  | bvsdiv  -- signed bit-vector division
  | bvudiv  -- unsigned bit-vector division
  | bvsrem  -- signed remainder (remainder of division rounded towards zero) (copies sign from dividend)
  | bvsmod  -- signed modulus (remainder of division rounded towards negative infinity) (copies sign from divisor)
  | bvurem  -- unsigned modulus
  | bvshl
  | bvlshr
  | bvslt
  | bvsle
  | bvult
  | bvule
  | bvnego  -- bit-vector negation overflow predicate
  | bvsaddo -- bit-vector signed addition overflow predicate
  | bvssubo -- bit-vector signed subtraction overflow predicate
  | bvsmulo -- bit-vector signed multiplication overflow predicate
  | zero_extend : Nat → Op
  ---------- CVC theory of finite sets (`FS`) ----------
  | set.member
  | set.subset
  | set.inter
  ---------- Core ADT operators with a trusted mapping to SMT ----------
  | option.get
  | record.get  : Attr → Op
  | string.like : Pattern → Op
  ---------- Extension ADT operators with a trusted mapping to SMT ----------
  | ext : ExtOp → Op
```

`Cedar.SymCC.UUF.lt` (definition, [line 106](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Op.lean#L106))

```lean
public def UUF.lt (uf uf' : UUF) : Bool
```

`Cedar.SymCC.UUF.decLt` (instance, [line 114](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Op.lean#L114))

```lean
public instance UUF.decLt (x y : UUF) : Decidable (x < y)
```

`Cedar.SymCC.ExtOp.lt` (definition, [line 129](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Op.lean#L129))

```lean
public def ExtOp.lt : ExtOp → ExtOp → Bool
```

`Cedar.SymCC.ExtOp.decLt` (instance, [line 135](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Op.lean#L135))

```lean
public instance ExtOp.decLt (x y : ExtOp) : Decidable (x < y)
```

`Cedar.SymCC.Op.mkName` (definition, [line 138](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Op.lean#L138))

```lean
public def Op.mkName : Op → String
```

`Cedar.SymCC.Op.lt` (definition, [line 173](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Op.lean#L173))

```lean
public def Op.lt : Op → Op → Bool
```

`Cedar.SymCC.Op.decLt` (instance, [line 184](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Op.lean#L184))

```lean
public instance Op.decLt (x y : Op) : Decidable (x < y)
```

## Depends on

- [Wildcard](../../spec/wildcard.md)
- [TermType](../part-02/termtype.md)

## Sources

- [Cedar/SymCC/Op.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Op.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.SymCC.Op.json)
