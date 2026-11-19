---
catalog: module
lean: Cedar.SymCC.Factory.noneOf, Cedar.SymCC.Factory.someOf, Cedar.SymCC.Factory.setOf, Cedar.SymCC.Factory.recordOf, Cedar.SymCC.Factory.tagOf, Cedar.SymCC.Factory.not, Cedar.SymCC.Factory.opposites, Cedar.SymCC.Factory.and, Cedar.SymCC.Factory.or, Cedar.SymCC.Factory.implies, Cedar.SymCC.Factory.eq, Cedar.SymCC.Factory.ite, Cedar.SymCC.Factory.app, Cedar.SymCC.Factory.bvneg, Cedar.SymCC.Factory.bvapp, Cedar.SymCC.Factory.bvadd, Cedar.SymCC.Factory.bvsub, Cedar.SymCC.Factory.bvmul, Cedar.SymCC.Factory.bvsdiv, Cedar.SymCC.Factory.bvudiv, Cedar.SymCC.Factory.bvsrem, Cedar.SymCC.Factory.bvsmod, Cedar.SymCC.Factory.bvurem, Cedar.SymCC.Factory.bvshl, Cedar.SymCC.Factory.bvlshr, Cedar.SymCC.Factory.bvcmp, Cedar.SymCC.Factory.bvslt, Cedar.SymCC.Factory.bvsle, Cedar.SymCC.Factory.bvult, Cedar.SymCC.Factory.bvule, Cedar.SymCC.Factory.bvnego, Cedar.SymCC.Factory.bvso, Cedar.SymCC.Factory.bvsaddo, Cedar.SymCC.Factory.bvssubo, Cedar.SymCC.Factory.bvsmulo, Cedar.SymCC.Factory.zero_extend, Cedar.SymCC.Factory.set.member, Cedar.SymCC.Factory.set.subset, Cedar.SymCC.Factory.set.inter, Cedar.SymCC.Factory.set.isEmpty, Cedar.SymCC.Factory.set.intersects, Cedar.SymCC.Factory.option.get, Cedar.SymCC.Factory.record.get, Cedar.SymCC.Factory.string.like, Cedar.SymCC.Factory.ext.decimal.val, Cedar.SymCC.Factory.ext.ipaddr.isV4, Cedar.SymCC.Factory.ext.ipaddr.addrV4, Cedar.SymCC.Factory.ext.ipaddr.prefixV4, Cedar.SymCC.Factory.ext.ipaddr.addrV6, Cedar.SymCC.Factory.ext.ipaddr.prefixV6, Cedar.SymCC.Factory.ext.datetime.val, Cedar.SymCC.Factory.ext.datetime.ofBitVec, Cedar.SymCC.Factory.ext.duration.val, Cedar.SymCC.Factory.ext.duration.ofBitVec, Cedar.SymCC.Factory.isNone, Cedar.SymCC.Factory.isSome, Cedar.SymCC.Factory.ifFalse, Cedar.SymCC.Factory.ifTrue, Cedar.SymCC.Factory.ifSome, Cedar.SymCC.Factory.anyTrue, Cedar.SymCC.Factory.anyNone, Cedar.SymCC.Factory.ifAllSome, Cedar.SymCC.Factory.bvaddChecked, Cedar.SymCC.Factory.bvsubChecked, Cedar.SymCC.Factory.bvmulChecked
statement: formalized
proof: formalized
---

# Factory

`Cedar.SymCC.Factory`, in [Cedar/SymCC/Factory.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean).

> This file defines an API for construcing well-formed Terms. In this basic
> implementation, the factory functions perform only basic partial
> evaluation---constant folding along with a few other rewrites.  In an optimized
> implementation, the factory functions would include more rewrite rules, and
> share a cache of partially cannonicalized terms that have been constructed so
> far.
>
> The factory functions are total. If given well-formed and type-correct
> arguments, a factory function will return a well-formed and type-correct output.
> Otherwise, the output is an arbitrary term.
>
> This design lets us minimize the number of error paths in the overall
> specification of symbolic compilation, which makes for nicer code and proofs, and
> it more closely tracks the specification of the concrete evaluator.
>
> See `Compiler.lean` to see how the symbolic compiler uses this API.

`Cedar.SymCC.Factory.noneOf` (definition, [line 51](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L51))

```lean
public def noneOf (ty : TermType) : Term
```

`Cedar.SymCC.Factory.someOf` (definition, [line 54](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L54))

```lean
public def someOf (t : Term) : Term
```

`Cedar.SymCC.Factory.setOf` (definition, [line 57](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L57))

```lean
public def setOf (ts : List Term) (ty : TermType) : Term
```

`Cedar.SymCC.Factory.recordOf` (definition, [line 59](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L59))

```lean
public def recordOf (ats : List (Attr × Term)) : Term
```

`Cedar.SymCC.Factory.tagOf` (definition, [line 61](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L61))

```lean
public def tagOf (entity tag : Term) : Term
```

`Cedar.SymCC.Factory.not` (definition, [line 65](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L65))

```lean
public def not : Term → Term
```

`Cedar.SymCC.Factory.opposites` (definition, [line 71](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L71))

```lean
public def opposites : Term → Term → Bool
```

`Cedar.SymCC.Factory.and` (definition, [line 76](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L76))

```lean
public def and (t₁ t₂ : Term) : Term
```

`Cedar.SymCC.Factory.or` (definition, [line 85](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L85))

```lean
public def or (t₁ t₂ : Term) : Term
```

`Cedar.SymCC.Factory.implies` (definition, [line 94](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L94))

```lean
public def implies (t₁ t₂ : Term) : Term
```

`Cedar.SymCC.Factory.eq` (definition, [line 98](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L98))

```lean
public def eq (t₁ t₂ : Term) : Term
```

`Cedar.SymCC.Factory.ite` (definition, [line 121](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L121))

```lean
public def ite (t₁ t₂ t₃ : Term) : Term
```

`Cedar.SymCC.Factory.app` (definition, [line 144](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L144))

```lean
public def app : UnaryFunction → Term → Term
```

`Cedar.SymCC.Factory.bvneg` (definition, [line 160](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L160))

```lean
public def bvneg : Term → Term
```

`Cedar.SymCC.Factory.bvapp` (definition, [line 166](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L166))

```lean
public def bvapp (op : Op) (fn : ∀ {n}, BitVec n → BitVec n → BitVec n) (t₁ t₂ : Term) : Term
```

`Cedar.SymCC.Factory.bvadd` (definition, [line 173](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L173))

```lean
public def bvadd
```

`Cedar.SymCC.Factory.bvsub` (definition, [line 174](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L174))

```lean
public def bvsub
```

`Cedar.SymCC.Factory.bvmul` (definition, [line 175](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L175))

```lean
public def bvmul
```

`Cedar.SymCC.Factory.bvsdiv` (definition, [line 176](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L176))

```lean
public def bvsdiv
```

`Cedar.SymCC.Factory.bvudiv` (definition, [line 177](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L177))

```lean
public def bvudiv
```

`Cedar.SymCC.Factory.bvsrem` (definition, [line 178](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L178))

```lean
public def bvsrem
```

`Cedar.SymCC.Factory.bvsmod` (definition, [line 179](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L179))

```lean
public def bvsmod
```

`Cedar.SymCC.Factory.bvurem` (definition, [line 180](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L180))

```lean
public def bvurem
```

`Cedar.SymCC.Factory.bvshl` (definition, [line 182](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L182))

```lean
public def bvshl
```

`Cedar.SymCC.Factory.bvlshr` (definition, [line 183](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L183))

```lean
public def bvlshr
```

`Cedar.SymCC.Factory.bvcmp` (definition, [line 186](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L186))

```lean
public def bvcmp (op : Op) (fn : ∀ {n}, BitVec n → BitVec n → Bool) (t₁ t₂ : Term) : Term
```

`Cedar.SymCC.Factory.bvslt` (definition, [line 193](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L193))

```lean
public def bvslt
```

`Cedar.SymCC.Factory.bvsle` (definition, [line 194](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L194))

```lean
public def bvsle
```

`Cedar.SymCC.Factory.bvult` (definition, [line 195](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L195))

```lean
public def bvult
```

`Cedar.SymCC.Factory.bvule` (definition, [line 196](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L196))

```lean
public def bvule
```

`Cedar.SymCC.Factory.bvnego` (definition, [line 198](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L198))

```lean
public def bvnego : Term → Term
```

`Cedar.SymCC.Factory.bvso` (definition, [line 203](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L203))

```lean
public def bvso (op : Op) (fn : Int → Int → Int) (t₁ t₂ : Term) : Term
```

`Cedar.SymCC.Factory.bvsaddo` (definition, [line 209](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L209))

```lean
public def bvsaddo
```

`Cedar.SymCC.Factory.bvssubo` (definition, [line 210](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L210))

```lean
public def bvssubo
```

`Cedar.SymCC.Factory.bvsmulo` (definition, [line 211](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L211))

```lean
public def bvsmulo
```

`Cedar.SymCC.Factory.zero_extend` (definition, [line 217](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L217))

```lean
public def zero_extend (n : Nat) : Term → Term
```

`Cedar.SymCC.Factory.set.member` (definition, [line 228](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L228))

```lean
public def set.member (t ts : Term) : Term
```

`Cedar.SymCC.Factory.set.subset` (definition, [line 237](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L237))

```lean
public def set.subset (sub sup : Term) : Term
```

`Cedar.SymCC.Factory.set.inter` (definition, [line 248](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L248))

```lean
public def set.inter (ts₁ ts₂ : Term) : Term
```

`Cedar.SymCC.Factory.set.isEmpty` (definition, [line 260](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L260))

```lean
public def set.isEmpty : Term → Term
```

`Cedar.SymCC.Factory.set.intersects` (definition, [line 267](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L267))

```lean
public def set.intersects (ts₁ ts₂ : Term) : Term
```

`Cedar.SymCC.Factory.option.get` (definition, [line 272](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L272))

```lean
public def option.get : Term → Term
```

`Cedar.SymCC.Factory.record.get` (definition, [line 279](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L279))

```lean
public def record.get (t : Term) (a : Attr) : Term
```

`Cedar.SymCC.Factory.string.like` (definition, [line 287](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L287))

```lean
public def string.like (t : Term) (p : Pattern) : Term
```

`Cedar.SymCC.Factory.ext.decimal.val` (definition, [line 294](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L294))

```lean
public def ext.decimal.val : Term → Term
```

`Cedar.SymCC.Factory.ext.ipaddr.isV4` (definition, [line 298](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L298))

```lean
public def ext.ipaddr.isV4 : Term → Term
```

`Cedar.SymCC.Factory.ext.ipaddr.addrV4` (definition, [line 302](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L302))

```lean
public def ext.ipaddr.addrV4 : Term → Term
```

`Cedar.SymCC.Factory.ext.ipaddr.prefixV4` (definition, [line 306](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L306))

```lean
public def ext.ipaddr.prefixV4 : Term → Term
```

`Cedar.SymCC.Factory.ext.ipaddr.addrV6` (definition, [line 313](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L313))

```lean
public def ext.ipaddr.addrV6 : Term → Term
```

`Cedar.SymCC.Factory.ext.ipaddr.prefixV6` (definition, [line 317](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L317))

```lean
public def ext.ipaddr.prefixV6 : Term → Term
```

`Cedar.SymCC.Factory.ext.datetime.val` (definition, [line 324](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L324))

```lean
public def ext.datetime.val : Term → Term
```

`Cedar.SymCC.Factory.ext.datetime.ofBitVec` (definition, [line 328](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L328))

```lean
public def ext.datetime.ofBitVec : Term -> Term
```

`Cedar.SymCC.Factory.ext.duration.val` (definition, [line 332](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L332))

```lean
public def ext.duration.val : Term → Term
```

`Cedar.SymCC.Factory.ext.duration.ofBitVec` (definition, [line 336](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L336))

```lean
public def ext.duration.ofBitVec : Term -> Term
```

`Cedar.SymCC.Factory.isNone` (definition, [line 342](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L342))

```lean
public def isNone : Term → Term
```

`Cedar.SymCC.Factory.isSome` (definition, [line 353](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L353))

```lean
public def isSome (t : Term) : Term
```

`Cedar.SymCC.Factory.ifFalse` (definition, [line 356](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L356))

```lean
public def ifFalse (g t : Term) : Term
```

`Cedar.SymCC.Factory.ifTrue` (definition, [line 359](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L359))

```lean
public def ifTrue (g t : Term) : Term
```

`Cedar.SymCC.Factory.ifSome` (definition, [line 362](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L362))

```lean
public def ifSome (g t : Term) : Term
```

`Cedar.SymCC.Factory.anyTrue` (definition, [line 367](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L367))

```lean
public def anyTrue (f : Term → Term) (ts : List Term) : Term
```

`Cedar.SymCC.Factory.anyNone` (definition, [line 370](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L370))

```lean
public def anyNone (gs : List Term) : Term
```

`Cedar.SymCC.Factory.ifAllSome` (definition, [line 372](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L372))

```lean
public def ifAllSome (gs : List Term) (t : Term) : Term
```

`Cedar.SymCC.Factory.bvaddChecked` (definition, [line 378](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L378))

```lean
public def bvaddChecked t₁ t₂
```

`Cedar.SymCC.Factory.bvsubChecked` (definition, [line 379](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L379))

```lean
public def bvsubChecked t₁ t₂
```

`Cedar.SymCC.Factory.bvmulChecked` (definition, [line 380](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean#L380))

```lean
public def bvmulChecked t₁ t₂
```

## Depends on

- [Function](function.md)

## Sources

- [Cedar/SymCC/Factory.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Factory.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.SymCC.Factory.json)
