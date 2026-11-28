---
catalog: module
lean: Mersenne31.Circle.OnCircle, Mersenne31.Circle.Point, Mersenne31.Circle.Point.ext, Mersenne31.Circle.Point.zero, Mersenne31.Circle.Point.conjugate, Mersenne31.Circle.Point.antipode, Mersenne31.Circle.Point.add, Mersenne31.Circle.Point.zero_x, Mersenne31.Circle.Point.zero_y, Mersenne31.Circle.Point.conjugate_x, Mersenne31.Circle.Point.conjugate_y, Mersenne31.Circle.Point.antipode_x, Mersenne31.Circle.Point.antipode_y, Mersenne31.Circle.Point.add_x, Mersenne31.Circle.Point.add_y, Mersenne31.Circle.generatorX, Mersenne31.Circle.generatorY, Mersenne31.Circle.generatorX_eq, Mersenne31.Circle.generatorY_eq, Mersenne31.Circle.generator_onCircle, Mersenne31.Circle.generator, Mersenne31.Circle.generator_x, Mersenne31.Circle.generator_y, Mersenne31.Circle.generator_half_order, Mersenne31.Circle.logOrder, Mersenne31.Circle.order, Mersenne31.Circle.order_nsmul_generator, Mersenne31.Circle.addOrderOf_generator, Mersenne31.Circle.CirclePointIndex, Mersenne31.Circle.CirclePointIndex.generator, Mersenne31.Circle.CirclePointIndex.generator_eq, Mersenne31.Circle.CirclePointIndex.subgroupGen, Mersenne31.Circle.CirclePointIndex.subgroupGen_eq, Mersenne31.Circle.CirclePointIndex.toPoint, Mersenne31.Circle.CirclePointIndex.toPoint_def, Mersenne31.Circle.CirclePointIndex.toPoint_zero, Mersenne31.Circle.CirclePointIndex.toPoint_generator, Mersenne31.Circle.CirclePointIndex.toPoint_one, Mersenne31.Circle.CirclePointIndex.toPoint_add, Mersenne31.Circle.CirclePointIndex.toPointHom, Mersenne31.Circle.CirclePointIndex.toPointHom_apply, Mersenne31.Circle.CirclePointIndex.toPoint_injective, Mersenne31.Circle.CirclePointIndex.toPoint_inj, Mersenne31.Circle.CirclePointIndex.addOrderOf_toPoint, Mersenne31.Circle.CirclePointIndex.addOrderOf_subgroupGen, Mersenne31.Circle.CirclePointIndex.toPoint_neg, Mersenne31.Circle.CirclePointIndex.toPoint_sub, Mersenne31.Circle.CirclePointIndex.subgroupGen_zero, Mersenne31.Circle.CirclePointIndex.subgroupGen_logOrder, Mersenne31.Circle.Coset, Mersenne31.Circle.Coset.new, Mersenne31.Circle.Coset.new_initialIndex, Mersenne31.Circle.Coset.new_stepSize, Mersenne31.Circle.Coset.new_logSize, Mersenne31.Circle.Coset.subgroup, Mersenne31.Circle.Coset.subgroup_eq, Mersenne31.Circle.Coset.odds, Mersenne31.Circle.Coset.odds_eq, Mersenne31.Circle.Coset.halfOdds, Mersenne31.Circle.Coset.halfOdds_eq, Mersenne31.Circle.Coset.size, Mersenne31.Circle.Coset.size_eq, Mersenne31.Circle.Coset.indexAt, Mersenne31.Circle.Coset.indexAt_eq, Mersenne31.Circle.Coset.pointAt, Mersenne31.Circle.Coset.pointAt_def, Mersenne31.Circle.Coset.Valid, Mersenne31.Circle.Coset.valid_iff, Mersenne31.Circle.Coset.new_valid, Mersenne31.Circle.Coset.subgroup_valid, Mersenne31.Circle.Coset.odds_valid, Mersenne31.Circle.Coset.halfOdds_valid, Mersenne31.Circle.Coset.indexAt_injective, Mersenne31.Circle.Coset.pointAt_injective, Mersenne31.Circle.Coset.card_range_indexAt, Mersenne31.Circle.Coset.card_range_pointAt, Mersenne31.Circle.Coset.conjugate, Mersenne31.Circle.Coset.indexAt_zero, Mersenne31.Circle.Coset.indexAt_succ, Mersenne31.Circle.Coset.conjugate_logSize, Mersenne31.Circle.Coset.conjugate_initialIndex, Mersenne31.Circle.Coset.conjugate_stepSize, Mersenne31.Circle.Coset.conjugate_valid_iff, Mersenne31.Circle.Coset.conjugate_indexAt, Mersenne31.Circle.CircleDomain, Mersenne31.Circle.CircleDomain.new, Mersenne31.Circle.CircleDomain.new_halfCoset, Mersenne31.Circle.CircleDomain.logSize, Mersenne31.Circle.CircleDomain.logSize_eq, Mersenne31.Circle.CircleDomain.size, Mersenne31.Circle.CircleDomain.size_eq, Mersenne31.Circle.CircleDomain.indexAt, Mersenne31.Circle.CircleDomain.indexAt_def, Mersenne31.Circle.CircleDomain.pointAt, Mersenne31.Circle.CircleDomain.pointAt_def, Mersenne31.Circle.CircleDomain.size_eq_two_mul_halfSize, Mersenne31.Circle.CircleDomain.indexAt_left, Mersenne31.Circle.CircleDomain.indexAt_of_le, Mersenne31.Circle.CircleDomain.indexAt_right, Mersenne31.Circle.CanonicCoset, Mersenne31.Circle.CanonicCoset.coset, Mersenne31.Circle.CanonicCoset.coset_eq, Mersenne31.Circle.CanonicCoset.halfCoset, Mersenne31.Circle.CanonicCoset.halfCoset_eq, Mersenne31.Circle.CanonicCoset.coset_valid, Mersenne31.Circle.CanonicCoset.halfCoset_valid, Mersenne31.Circle.CanonicCoset.circleDomain, Mersenne31.Circle.CanonicCoset.circleDomain_eq, Mersenne31.Circle.CanonicCoset.circleDomain_logSize, Mersenne31.Circle.CanonicCoset.circleDomain_size
statement: formalized
proof: formalized
---

# Mersenne31 Circle Domains

`CompPoly.Fields.Mersenne31.Circle`, in [CompPoly/Fields/Mersenne31/Circle.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean), by Adrien Lacombe.

> This module mirrors the structural circle-domain layer used by STWO over the
> Mersenne31 field. It records the circle equation, the STWO M31 circle generator,
> index arithmetic modulo the circle order, and the coset/domain shapes used by
> canonical circle domains.
>
> Circle points form an additive commutative group, with binary scalar multiplication.
> The STWO generator has order `2^31`, and `CirclePointIndex.toPoint` is injective and
> respects addition. Each subgroup step has the requested exact order.
>
> `Coset.Valid` requires the step order to equal the declared size. Standard constructors
> satisfy it; valid cosets enumerate distinct indices and points and have the declared
> range cardinality. Circle domains still need a validity condition requiring disjoint
> halves before their declared size can be identified with set cardinality.

`Mersenne31.Circle.OnCircle` (definition, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L38))

> Predicate for points on the circle `x^2 + y^2 = 1`.

```lean
def OnCircle (x y : Field) : Prop
```

`Mersenne31.Circle.Point` (structure, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L46))

> A point on the Mersenne31 circle.

```lean
structure Point where
  x : Field
  y : Field
  onCircle : OnCircle x y
```

`Mersenne31.Circle.Point.ext` (theorem, [line 55](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L55))

> Two circle points are equal when both coordinates are equal.

```lean
theorem ext {p q : Point} (hx : p.x = q.x) (hy : p.y = q.y) : p = q
```

`Mersenne31.Circle.Point.zero` (definition, [line 61](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L61))

> The identity point of the circle group.

```lean
def zero : Point
```

`Mersenne31.Circle.Point.conjugate` (definition, [line 68](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L68))

> The circle-group inverse, equal to complex conjugation.

```lean
def conjugate (p : Point) : Point
```

`Mersenne31.Circle.Point.antipode` (definition, [line 75](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L75))

> The antipodal point, obtained by negating both coordinates.

```lean
def antipode (p : Point) : Point
```

`Mersenne31.Circle.Point.add` (definition, [line 82](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L82))

> Circle-group addition, written as multiplication of complex coordinates.

```lean
def add (p q : Point) : Point
```

`Mersenne31.Circle.Point.zero_x` (theorem, [line 112](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L112))

> The identity point has x-coordinate one.

```lean
theorem zero_x : (0 : Point).x = 1
```

`Mersenne31.Circle.Point.zero_y` (theorem, [line 116](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L116))

> The identity point has y-coordinate zero.

```lean
theorem zero_y : (0 : Point).y = 0
```

`Mersenne31.Circle.Point.conjugate_x` (theorem, [line 120](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L120))

> Conjugation preserves the x-coordinate.

```lean
theorem conjugate_x (p : Point) : (-p).x = p.x
```

`Mersenne31.Circle.Point.conjugate_y` (theorem, [line 124](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L124))

> Conjugation negates the y-coordinate.

```lean
theorem conjugate_y (p : Point) : (-p).y = -p.y
```

`Mersenne31.Circle.Point.antipode_x` (theorem, [line 128](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L128))

> The antipode negates the x-coordinate.

```lean
theorem antipode_x (p : Point) : p.antipode.x = -p.x
```

`Mersenne31.Circle.Point.antipode_y` (theorem, [line 132](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L132))

> The antipode negates the y-coordinate.

```lean
theorem antipode_y (p : Point) : p.antipode.y = -p.y
```

`Mersenne31.Circle.Point.add_x` (theorem, [line 136](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L136))

> The x-coordinate of circle addition.

```lean
theorem add_x (p q : Point) : (p + q).x = p.x * q.x - p.y * q.y
```

`Mersenne31.Circle.Point.add_y` (theorem, [line 140](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L140))

> The y-coordinate of circle addition.

```lean
theorem add_y (p q : Point) : (p + q).y = p.x * q.y + p.y * q.x
```

`Mersenne31.Circle.generatorX` (definition, [line 179](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L179))

> STWO's Mersenne31 circle generator x-coordinate.

```lean
def generatorX : Field
```

`Mersenne31.Circle.generatorY` (definition, [line 182](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L182))

> STWO's Mersenne31 circle generator y-coordinate.

```lean
def generatorY : Field
```

`Mersenne31.Circle.generatorX_eq` (theorem, [line 186](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L186))

> The STWO generator's x-coordinate constant is two.

```lean
theorem generatorX_eq : generatorX = 2
```

`Mersenne31.Circle.generatorY_eq` (theorem, [line 190](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L190))

> The value of the STWO generator's y-coordinate constant.

```lean
theorem generatorY_eq : generatorY = 1268011823
```

`Mersenne31.Circle.generator_onCircle` (theorem, [line 193](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L193))

> STWO's Mersenne31 circle generator lies on `x^2 + y^2 = 1`.

```lean
theorem generator_onCircle : OnCircle generatorX generatorY
```

`Mersenne31.Circle.generator` (definition, [line 198](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L198))

> STWO's generator for the Mersenne31 circle group.

```lean
def generator : Point
```

`Mersenne31.Circle.generator_x` (theorem, [line 205](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L205))

> The STWO generator has x-coordinate two.

```lean
theorem generator_x : generator.x = 2
```

`Mersenne31.Circle.generator_y` (theorem, [line 209](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L209))

> The STWO generator's y-coordinate.

```lean
theorem generator_y : generator.y = 1268011823
```

`Mersenne31.Circle.generator_half_order` (theorem, [line 252](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L252))

> The half-order multiple of the STWO generator is the antipode of the identity.

```lean
theorem generator_half_order : (2 ^ 30 : Nat) • generator = Point.antipode 0
```

`Mersenne31.Circle.logOrder` (definition, [line 261](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L261))

> The log order of STWO's Mersenne31 circle group.

```lean
def logOrder : Nat
```

`Mersenne31.Circle.order` (definition, [line 265](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L265))

> The order of the Mersenne31 circle-index group, `2^31`.

```lean
def order : Nat
```

`Mersenne31.Circle.order_nsmul_generator` (theorem, [line 268](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L268))

> The circle-index modulus annihilates the STWO generator.

```lean
theorem order_nsmul_generator : order • generator = 0
```

`Mersenne31.Circle.addOrderOf_generator` (theorem, [line 281](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L281))

> The STWO Mersenne31 circle generator has exact additive order `2^31`.

```lean
theorem addOrderOf_generator : addOrderOf generator = 2 ^ 31
```

`Mersenne31.Circle.CirclePointIndex` (abbreviation, [line 290](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L290))

> Integer index for multiples of the Mersenne31 circle generator.

```lean
abbrev CirclePointIndex
```

`Mersenne31.Circle.CirclePointIndex.generator` (definition, [line 295](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L295))

> The distinguished generator index.

```lean
def generator : CirclePointIndex
```

`Mersenne31.Circle.CirclePointIndex.generator_eq` (theorem, [line 299](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L299))

> The distinguished generator index is one.

```lean
theorem generator_eq : generator = 1
```

`Mersenne31.Circle.CirclePointIndex.subgroupGen` (definition, [line 303](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L303))

> Subgroup generator index for the subgroup of order `2^logSize`.
> The explicit bound rules out truncated subtraction for out-of-range inputs.

```lean
def subgroupGen (logSize : Nat) (_hlogSize : logSize ≤ logOrder) : CirclePointIndex
```

`Mersenne31.Circle.CirclePointIndex.subgroupGen_eq` (theorem, [line 307](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L307))

> The subgroup step is the corresponding power of two modulo the circle order.

```lean
theorem subgroupGen_eq (logSize : Nat) (h : logSize ≤ logOrder) :
    subgroupGen logSize h = ((2 ^ (logOrder - logSize) : Nat) : CirclePointIndex)
```

`Mersenne31.Circle.CirclePointIndex.toPoint` (definition, [line 311](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L311))

> Interpret the canonical representative of an index as a multiple of the STWO generator.

```lean
def toPoint (i : CirclePointIndex) : Point
```

`Mersenne31.Circle.CirclePointIndex.toPoint_def` (theorem, [line 315](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L315))

> Index interpretation uses the canonical natural representative.

```lean
theorem toPoint_def (i : CirclePointIndex) :
    toPoint i = i.val • Circle.generator
```

`Mersenne31.Circle.CirclePointIndex.toPoint_zero` (theorem, [line 320](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L320))

> Index zero maps to the circle identity.

```lean
theorem toPoint_zero : toPoint 0 = 0
```

`Mersenne31.Circle.CirclePointIndex.toPoint_generator` (theorem, [line 326](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L326))

> The distinguished index maps to the STWO circle generator.

```lean
theorem toPoint_generator : toPoint CirclePointIndex.generator = Circle.generator
```

`Mersenne31.Circle.CirclePointIndex.toPoint_one` (theorem, [line 332](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L332))

> Index one maps to the STWO circle generator.

```lean
theorem toPoint_one : toPoint 1 = Circle.generator
```

`Mersenne31.Circle.CirclePointIndex.toPoint_add` (theorem, [line 337](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L337))

> Index addition agrees with circle addition, including wraparound at the circle order.

```lean
theorem toPoint_add (i j : CirclePointIndex) : toPoint (i + j) = toPoint i + toPoint j
```

`Mersenne31.Circle.CirclePointIndex.toPointHom` (definition, [line 343](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L343))

> The additive homomorphism interpreting circle indices as points.

```lean
def toPointHom : CirclePointIndex →+ Point
```

`Mersenne31.Circle.CirclePointIndex.toPointHom_apply` (theorem, [line 350](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L350))

> The homomorphism uses the executable index interpretation.

```lean
theorem toPointHom_apply (i : CirclePointIndex) : toPointHom i = toPoint i
```

`Mersenne31.Circle.CirclePointIndex.toPoint_injective` (theorem, [line 353](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L353))

> Different circle indices represent different points.

```lean
theorem toPoint_injective : Function.Injective toPoint
```

`Mersenne31.Circle.CirclePointIndex.toPoint_inj` (theorem, [line 363](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L363))

> Equality of interpreted points is exactly equality of their indices.

```lean
theorem toPoint_inj {i j : CirclePointIndex} : toPoint i = toPoint j ↔ i = j
```

`Mersenne31.Circle.CirclePointIndex.addOrderOf_toPoint` (theorem, [line 367](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L367))

> Interpreting an index preserves its additive order.

```lean
theorem addOrderOf_toPoint (i : CirclePointIndex) :
    addOrderOf (toPoint i) = addOrderOf i
```

`Mersenne31.Circle.CirclePointIndex.addOrderOf_subgroupGen` (theorem, [line 372](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L372))

> The subgroup step has the requested exact order, including log sizes zero and 31.

```lean
theorem addOrderOf_subgroupGen (n : Nat) (h : n ≤ logOrder) :
    addOrderOf (subgroupGen n h) = 2 ^ n
```

`Mersenne31.Circle.CirclePointIndex.toPoint_neg` (theorem, [line 384](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L384))

> Negating an index conjugates its circle point.

```lean
theorem toPoint_neg (i : CirclePointIndex) : toPoint (-i) = -toPoint i
```

`Mersenne31.Circle.CirclePointIndex.toPoint_sub` (theorem, [line 389](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L389))

> Subtracting indices agrees with subtracting their circle points.

```lean
theorem toPoint_sub (i j : CirclePointIndex) : toPoint (i - j) = toPoint i - toPoint j
```

`Mersenne31.Circle.CirclePointIndex.subgroupGen_zero` (theorem, [line 394](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L394))

> The subgroup generator for the trivial subgroup is zero modulo the circle order.

```lean
theorem subgroupGen_zero (h : 0 ≤ logOrder) : subgroupGen 0 h = 0
```

`Mersenne31.Circle.CirclePointIndex.subgroupGen_logOrder` (theorem, [line 400](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L400))

> The full-order subgroup generator is the distinguished generator index.

```lean
theorem subgroupGen_logOrder (h : logOrder ≤ logOrder) :
    subgroupGen logOrder h = generator
```

`Mersenne31.Circle.Coset` (structure, [line 409](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L409))

> An indexing shape with a fixed additive step.
> No relation between `stepSize` and `logSize` is required; a zero step is allowed.
> `Coset.Valid` supplies the exact-order condition for distinctness and cardinality.

```lean
structure Coset where
  initialIndex : CirclePointIndex
  stepSize : CirclePointIndex
  logSize : Nat
  logSize_le_logOrder : logSize ≤ logOrder
```

`Mersenne31.Circle.Coset.new` (definition, [line 418](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L418))

> Create a coset with STWO's subgroup step for `logSize`.

```lean
def new (initialIndex : CirclePointIndex) (logSize : Nat) (hlogSize : logSize ≤ logOrder) :
    Coset
```

`Mersenne31.Circle.Coset.new_initialIndex` (theorem, [line 427](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L427))

> The coset constructor preserves the initial index.

```lean
theorem new_initialIndex (i : CirclePointIndex) (n : Nat) (h : n ≤ logOrder) :
    (new i n h).initialIndex = i
```

`Mersenne31.Circle.Coset.new_stepSize` (theorem, [line 432](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L432))

> The coset constructor uses the subgroup generator as its step.

```lean
theorem new_stepSize (i : CirclePointIndex) (n : Nat) (h : n ≤ logOrder) :
    (new i n h).stepSize = CirclePointIndex.subgroupGen n h
```

`Mersenne31.Circle.Coset.new_logSize` (theorem, [line 437](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L437))

> The coset constructor preserves the log size.

```lean
theorem new_logSize (i : CirclePointIndex) (n : Nat) (h : n ≤ logOrder) :
    (new i n h).logSize = n
```

`Mersenne31.Circle.Coset.subgroup` (definition, [line 441](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L441))

> The additive subgroup of size `2^logSize`.

```lean
def subgroup (logSize : Nat) (hlogSize : logSize ≤ logOrder) : Coset
```

`Mersenne31.Circle.Coset.subgroup_eq` (theorem, [line 445](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L445))

> A subgroup is the coset starting at zero.

```lean
theorem subgroup_eq (n : Nat) (h : n ≤ logOrder) : subgroup n h = new 0 n h
```

`Mersenne31.Circle.Coset.odds` (definition, [line 448](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L448))

> The STWO coset `G_{2n} + <G_n>`.

```lean
def odds (logSize : Nat) (hlogSize : logSize + 1 ≤ logOrder) : Coset
```

`Mersenne31.Circle.Coset.odds_eq` (theorem, [line 453](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L453))

> The odds coset starts at the next larger subgroup's generator.

```lean
theorem odds_eq (n : Nat) (h : n + 1 ≤ logOrder) :
    odds n h = new (CirclePointIndex.subgroupGen (n + 1) h) n
      (Nat.le_trans (Nat.le_succ n) h)
```

`Mersenne31.Circle.Coset.halfOdds` (definition, [line 458](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L458))

> The STWO coset `G_{4n} + <G_n>`, whose conjugate completes `odds (logSize + 1)`.

```lean
def halfOdds (logSize : Nat) (hlogSize : logSize + 2 ≤ logOrder) : Coset
```

`Mersenne31.Circle.Coset.halfOdds_eq` (theorem, [line 463](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L463))

> The half-odds coset starts two subgroup levels above its step.

```lean
theorem halfOdds_eq (n : Nat) (h : n + 2 ≤ logOrder) :
    halfOdds n h = new (CirclePointIndex.subgroupGen (n + 2) h) n
      (Nat.le_trans (Nat.le_add_right n 2) h)
```

`Mersenne31.Circle.Coset.size` (definition, [line 468](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L468))

> Declared number of index positions, not necessarily the number of distinct points.

```lean
def size (c : Coset) : Nat
```

`Mersenne31.Circle.Coset.size_eq` (theorem, [line 473](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L473))

> A coset's size is two to its log size.

```lean
theorem size_eq (c : Coset) : c.size = 2 ^ c.logSize
```

`Mersenne31.Circle.Coset.indexAt` (definition, [line 476](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L476))

> The `i`th index in the coset order.

```lean
def indexAt (c : Coset) (i : Nat) : CirclePointIndex
```

`Mersenne31.Circle.Coset.indexAt_eq` (theorem, [line 482](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L482))

> Closed-form coset indexing, without recursive expansion of literal indices.
> Lower priority lets the zero and conjugation lemmas simplify first.

```lean
theorem indexAt_eq (c : Coset) (i : Nat) :
    c.indexAt i = c.initialIndex + c.stepSize * (i : CirclePointIndex)
```

`Mersenne31.Circle.Coset.pointAt` (definition, [line 486](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L486))

> The circle point at the `i`th coset index.

```lean
def pointAt (c : Coset) (i : Nat) : Point
```

`Mersenne31.Circle.Coset.pointAt_def` (theorem, [line 490](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L490))

> A coset point is the interpretation of its index.

```lean
theorem pointAt_def (c : Coset) (i : Nat) :
    c.pointAt i = CirclePointIndex.toPoint (c.indexAt i)
```

`Mersenne31.Circle.Coset.Valid` (definition, [line 494](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L494))

> The step has exactly as many distinct multiples as the declared coset size.

```lean
def Valid (c : Coset) : Prop
```

`Mersenne31.Circle.Coset.valid_iff` (theorem, [line 497](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L497))

> Validity is an exact-order condition on the step, independent of the initial index.

```lean
theorem valid_iff (c : Coset) : c.Valid ↔ addOrderOf c.stepSize = c.size
```

`Mersenne31.Circle.Coset.new_valid` (theorem, [line 500](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L500))

> The standard constructor uses a step of the requested order.

```lean
theorem new_valid (i : CirclePointIndex) (n : Nat) (h : n ≤ logOrder) :
    (new i n h).Valid
```

`Mersenne31.Circle.Coset.subgroup_valid` (theorem, [line 506](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L506))

> The subgroup constructor has a step of the declared order.

```lean
theorem subgroup_valid (n : Nat) (h : n ≤ logOrder) : (subgroup n h).Valid
```

`Mersenne31.Circle.Coset.odds_valid` (theorem, [line 511](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L511))

> The odds constructor has a step of the declared order.

```lean
theorem odds_valid (n : Nat) (h : n + 1 ≤ logOrder) : (odds n h).Valid
```

`Mersenne31.Circle.Coset.halfOdds_valid` (theorem, [line 516](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L516))

> The half-odds constructor has a step of the declared order.

```lean
theorem halfOdds_valid (n : Nat) (h : n + 2 ≤ logOrder) : (halfOdds n h).Valid
```

`Mersenne31.Circle.Coset.indexAt_injective` (theorem, [line 521](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L521))

> Valid cosets enumerate distinct indices within their declared size.

```lean
theorem indexAt_injective (c : Coset) (hc : c.Valid) :
    Function.Injective (fun i : Fin c.size => c.indexAt i.val)
```

`Mersenne31.Circle.Coset.pointAt_injective` (theorem, [line 532](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L532))

> Valid cosets enumerate distinct circle points within their declared size.

```lean
theorem pointAt_injective (c : Coset) (hc : c.Valid) :
    Function.Injective (fun i : Fin c.size => c.pointAt i.val)
```

`Mersenne31.Circle.Coset.card_range_indexAt` (theorem, [line 540](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L540))

> The bounded index range of a valid coset has its declared cardinality.

```lean
theorem card_range_indexAt (c : Coset) (hc : c.Valid) :
    Nat.card (Set.range (fun i : Fin c.size => c.indexAt i.val)) = c.size
```

`Mersenne31.Circle.Coset.card_range_pointAt` (theorem, [line 545](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L545))

> The bounded point range of a valid coset has its declared cardinality.

```lean
theorem card_range_pointAt (c : Coset) (hc : c.Valid) :
    Nat.card (Set.range (fun i : Fin c.size => c.pointAt i.val)) = c.size
```

`Mersenne31.Circle.Coset.conjugate` (definition, [line 550](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L550))

> The conjugate coset `-initial - <step>`.

```lean
def conjugate (c : Coset) : Coset
```

`Mersenne31.Circle.Coset.indexAt_zero` (theorem, [line 558](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L558))

> The first coset index is its initial index.

```lean
theorem indexAt_zero (c : Coset) : c.indexAt 0 = c.initialIndex
```

`Mersenne31.Circle.Coset.indexAt_succ` (theorem, [line 562](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L562))

> Successive coset indices differ by the fixed step size.

```lean
theorem indexAt_succ (c : Coset) (i : Nat) :
    c.indexAt (i + 1) = c.indexAt i + c.stepSize
```

`Mersenne31.Circle.Coset.conjugate_logSize` (theorem, [line 569](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L569))

> Conjugation preserves the coset log size.

```lean
theorem conjugate_logSize (c : Coset) : c.conjugate.logSize = c.logSize
```

`Mersenne31.Circle.Coset.conjugate_initialIndex` (theorem, [line 573](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L573))

> The conjugate coset starts at the negated initial index.

```lean
theorem conjugate_initialIndex (c : Coset) :
    c.conjugate.initialIndex = -c.initialIndex
```

`Mersenne31.Circle.Coset.conjugate_stepSize` (theorem, [line 578](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L578))

> The conjugate coset uses the negated step size.

```lean
theorem conjugate_stepSize (c : Coset) : c.conjugate.stepSize = -c.stepSize
```

`Mersenne31.Circle.Coset.conjugate_valid_iff` (theorem, [line 582](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L582))

> Conjugation preserves the exact-order condition.

```lean
theorem conjugate_valid_iff (c : Coset) : c.conjugate.Valid ↔ c.Valid
```

`Mersenne31.Circle.Coset.conjugate_indexAt` (theorem, [line 587](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L587))

> Each conjugate-coset index is the negation of the corresponding original index.

```lean
theorem conjugate_indexAt (c : Coset) (i : Nat) :
    c.conjugate.indexAt i = -c.indexAt i
```

`Mersenne31.Circle.CircleDomain` (structure, [line 597](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L597))

> A domain indexing shape: a half coset followed by its conjugate.
> The halves need not be disjoint, and either half may contain repeated points.
> A follow-up must impose validity conditions before identifying `size` with cardinality.

```lean
structure CircleDomain where
  halfCoset : Coset
```

`Mersenne31.Circle.CircleDomain.new` (definition, [line 603](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L603))

> Construct a circle domain from the half coset.

```lean
def new (halfCoset : Coset) : CircleDomain
```

`Mersenne31.Circle.CircleDomain.new_halfCoset` (theorem, [line 608](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L608))

> The domain constructor preserves its half coset.

```lean
theorem new_halfCoset (c : Coset) : (new c).halfCoset = c
```

`Mersenne31.Circle.CircleDomain.logSize` (definition, [line 611](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L611))

> Domain log size. A domain contains a half coset and its conjugate.

```lean
def logSize (D : CircleDomain) : Nat
```

`Mersenne31.Circle.CircleDomain.logSize_eq` (theorem, [line 616](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L616))

> A domain's log size is one more than its half coset's log size.

```lean
theorem logSize_eq (D : CircleDomain) : D.logSize = D.halfCoset.logSize + 1
```

`Mersenne31.Circle.CircleDomain.size` (definition, [line 619](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L619))

> Declared number of index positions, not necessarily the number of distinct points.

```lean
def size (D : CircleDomain) : Nat
```

`Mersenne31.Circle.CircleDomain.size_eq` (theorem, [line 623](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L623))

> A domain's size is two to its log size.

```lean
theorem size_eq (D : CircleDomain) : D.size = 2 ^ D.logSize
```

`Mersenne31.Circle.CircleDomain.indexAt` (definition, [line 626](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L626))

> The `i`th domain index: first the half coset, then the conjugate coset.

```lean
def indexAt (D : CircleDomain) (i : Nat) : CirclePointIndex
```

`Mersenne31.Circle.CircleDomain.indexAt_def` (theorem, [line 633](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L633))

> Domain indexing splits at the half-coset size.

```lean
theorem indexAt_def (D : CircleDomain) (i : Nat) :
    D.indexAt i = if i < D.halfCoset.size then D.halfCoset.indexAt i
      else D.halfCoset.conjugate.indexAt (i - D.halfCoset.size)
```

`Mersenne31.Circle.CircleDomain.pointAt` (definition, [line 638](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L638))

> The circle point at the `i`th domain index.

```lean
def pointAt (D : CircleDomain) (i : Nat) : Point
```

`Mersenne31.Circle.CircleDomain.pointAt_def` (theorem, [line 642](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L642))

> A domain point is the interpretation of its index.

```lean
theorem pointAt_def (D : CircleDomain) (i : Nat) :
    D.pointAt i = CirclePointIndex.toPoint (D.indexAt i)
```

`Mersenne31.Circle.CircleDomain.size_eq_two_mul_halfSize` (theorem, [line 647](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L647))

> A circle domain has twice as many indices as its half coset.

```lean
theorem size_eq_two_mul_halfSize (D : CircleDomain) :
    D.size = 2 * D.halfCoset.size
```

`Mersenne31.Circle.CircleDomain.indexAt_left` (theorem, [line 653](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L653))

> Indices in the first half of a circle domain come from its half coset.

```lean
theorem indexAt_left (D : CircleDomain) (i : Nat) (hi : i < D.halfCoset.size) :
    D.indexAt i = D.halfCoset.indexAt i
```

`Mersenne31.Circle.CircleDomain.indexAt_of_le` (theorem, [line 659](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L659))

> Indices at or beyond the half-coset size come from the conjugate half.

```lean
theorem indexAt_of_le (D : CircleDomain) (i : Nat) (hi : D.halfCoset.size ≤ i) :
    D.indexAt i = -D.halfCoset.indexAt (i - D.halfCoset.size)
```

`Mersenne31.Circle.CircleDomain.indexAt_right` (theorem, [line 665](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L665))

> Indices in the second half come from the negated half coset.

```lean
theorem indexAt_right (D : CircleDomain) (i : Nat) :
    D.indexAt (D.halfCoset.size + i) = -D.halfCoset.indexAt i
```

`Mersenne31.Circle.CanonicCoset` (structure, [line 672](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L672))

> A canonical STWO coset `G_{2n} + <G_n>` for `1 ≤ logSize < logOrder`.

```lean
structure CanonicCoset where
  logSize : Nat
  one_le_logSize : 1 ≤ logSize
  logSize_succ_le_logOrder : logSize + 1 ≤ logOrder
```

`Mersenne31.Circle.CanonicCoset.coset` (definition, [line 680](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L680))

> The full canonical coset `G_{2n} + <G_n>`.

```lean
def coset (c : CanonicCoset) : Coset
```

`Mersenne31.Circle.CanonicCoset.coset_eq` (theorem, [line 684](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L684))

> A canonical coset is the odds coset at its log size.

```lean
theorem coset_eq (c : CanonicCoset) :
    c.coset = Coset.odds c.logSize c.logSize_succ_le_logOrder
```

`Mersenne31.Circle.CanonicCoset.halfCoset` (definition, [line 688](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L688))

> The half coset used to form the canonical circle domain.

```lean
def halfCoset (c : CanonicCoset) : Coset
```

`Mersenne31.Circle.CanonicCoset.halfCoset_eq` (theorem, [line 697](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L697))

> The canonical half coset is the half-odds coset one log size below.

```lean
theorem halfCoset_eq (c : CanonicCoset) :
    c.halfCoset = Coset.halfOdds (c.logSize - 1) (by
      have hOne := c.one_le_logSize
      have hBound := c.logSize_succ_le_logOrder
      omega)
```

`Mersenne31.Circle.CanonicCoset.coset_valid` (theorem, [line 704](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L704))

> The full canonical coset has a step of the declared order.

```lean
theorem coset_valid (c : CanonicCoset) : c.coset.Valid
```

`Mersenne31.Circle.CanonicCoset.halfCoset_valid` (theorem, [line 709](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L709))

> The canonical half coset has a step of the declared order.

```lean
theorem halfCoset_valid (c : CanonicCoset) : c.halfCoset.Valid
```

`Mersenne31.Circle.CanonicCoset.circleDomain` (definition, [line 714](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L714))

> The canonical circle domain with the same log size.

```lean
def circleDomain (c : CanonicCoset) : CircleDomain
```

`Mersenne31.Circle.CanonicCoset.circleDomain_eq` (theorem, [line 718](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L718))

> The canonical domain is built from the canonical half coset.

```lean
theorem circleDomain_eq (c : CanonicCoset) :
    c.circleDomain = CircleDomain.new c.halfCoset
```

`Mersenne31.Circle.CanonicCoset.circleDomain_logSize` (theorem, [line 723](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L723))

> The canonical circle domain preserves the canonical coset log size.

```lean
theorem circleDomain_logSize (c : CanonicCoset) : c.circleDomain.logSize = c.logSize
```

`Mersenne31.Circle.CanonicCoset.circleDomain_size` (theorem, [line 731](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean#L731))

> The canonical circle domain has `2^logSize` indices.

```lean
theorem circleDomain_size (c : CanonicCoset) : c.circleDomain.size = 2 ^ c.logSize
```

## Depends on

- [Mersenne prime field `2^{31} - 1`](basic.md)

## Sources

- [CompPoly/Fields/Mersenne31/Circle.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Circle.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Mersenne31.Circle.json)
