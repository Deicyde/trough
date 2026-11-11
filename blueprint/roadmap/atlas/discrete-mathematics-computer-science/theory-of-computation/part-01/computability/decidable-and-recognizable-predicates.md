---
declaration: section
origin: cited
lean: MetaMathlibExt.ComputablePred.and, MetaMathlibExt.ComputablePred.or, MetaMathlibExt.REPred.and, MetaMathlibExt.REPred.or, MetaMathlibExt.REPred.exists_mem, MetaMathlibExt.REPred.forall_mem, MetaMathlibExt.computable_list_any, MetaMathlibExt.REPred.exists_partrec_choose
statement: formalized
proof: formalized
---

# Decidable and recognizable predicates

35 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html).

## Computable predicates are closed under conjunction

Let $\alpha$ be a type with a
primitive recursive encoding into $\mathbb{N}$. If $p$ and $q$ are computable predicates on
$\alpha$, then the predicate $a \mapsto p(a) \land q(a)$ is computable.

Formalized by `MetaMathlibExt.ComputablePred.and`, a theorem declared in [MathlibExt/Computability/RE.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Computability/RE.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#and).

## Computable predicates are closed under disjunction

Let $\alpha$ be a type with a
primitive recursive encoding into $\mathbb{N}$. If $p$ and $q$ are computable predicates on
$\alpha$, then the predicate $a \mapsto p(a) \lor q(a)$ is computable.

Formalized by `MetaMathlibExt.ComputablePred.or`, a theorem declared in [MathlibExt/Computability/RE.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Computability/RE.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#or).

## Recursively enumerable predicates are closed under conjunction

Let $\alpha$ be a type
with a primitive recursive encoding into $\mathbb{N}$. If $p$ and $q$ are recursively enumerable
predicates on $\alpha$, then the predicate $a \mapsto p(a) \land q(a)$ is recursively enumerable.

The proof runs one semi-decision procedure, then the other.

Formalized by `MetaMathlibExt.REPred.and`, a theorem declared in [MathlibExt/Computability/RE.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Computability/RE.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#and-2).

## Recursively enumerable predicates are closed under disjunction

Let $\alpha$ be a type
with a primitive recursive encoding into $\mathbb{N}$. If $p$ and $q$ are recursively enumerable
predicates on $\alpha$, then the predicate $a \mapsto p(a) \lor q(a)$ is recursively enumerable.

The proof runs both semi-decision procedures in parallel.

Formalized by `MetaMathlibExt.REPred.or`, a theorem declared in [MathlibExt/Computability/RE.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Computability/RE.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#or-2).

## Bounded existential quantification preserves recursive enumerability

Let $\alpha$ and
$\beta$ be types with primitive recursive encodings into $\mathbb{N}$, let $R$ be a relation
between $\alpha$ and $\beta$ that is recursively enumerable as a predicate on pairs $(a, b)$, and
let $c$ be a primitive recursive function sending each $a \in \alpha$ to a finite list $c(a)$ of
elements of $\beta$. Then the predicate $a \mapsto \exists b \in c(a),\ R(a, b)$ is recursively
enumerable.

The proof is by dovetailing: it searches for a step bound $k$ at which the simulation of the
semi-decision procedure for $R$ halts on $(a, b)$ for some $b$ in $c(a)$.

Formalized by `MetaMathlibExt.REPred.exists_mem`, a theorem declared in [MathlibExt/Computability/RE.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Computability/RE.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#exists-mem).

## Bounded universal quantification preserves recursive enumerability

Let $\alpha$ and
$\beta$ be types with primitive recursive encodings into $\mathbb{N}$, let $R$ be a relation
between $\alpha$ and $\beta$ that is recursively enumerable as a predicate on pairs $(a, b)$, and
let $c$ be a primitive recursive function sending each $a \in \alpha$ to a finite list $c(a)$ of
elements of $\beta$. Then the predicate $a \mapsto \forall b \in c(a),\ R(a, b)$ is recursively
enumerable.

The proof searches for one step bound $k$ at which the simulation of the semi-decision procedure
for $R$ halts on $(a, b)$ for every $b$ in $c(a)$; the step-bounded simulation is monotone in $k$.

Formalized by `MetaMathlibExt.REPred.forall_mem`, a theorem declared in [MathlibExt/Computability/RE.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Computability/RE.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#forall-mem).

## Searching a computable list with a computable test is computable

Let $\gamma$ and
$\beta$ be types with primitive recursive encodings into $\mathbb{N}$, let $l$ be a computable
function sending each $x \in \gamma$ to a finite list $l(x)$ of elements of $\beta$, and let $g$
be a computable Boolean-valued function of $x \in \gamma$ and $b \in \beta$. Then the
Boolean-valued function that sends $x$ to true exactly when $g(x, b)$ is true for some $b$ in
$l(x)$ is computable.

The proof scans the indices of $l(x)$ by primitive recursion.

Formalized by `MetaMathlibExt.computable_list_any`, a theorem declared in [MathlibExt/Computability/RE.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Computability/RE.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#computable-list-any).

## Selection for r.e. relations

Let $\alpha$ and $\beta$ be types with primitive recursive
encodings into $\mathbb{N}$, and let $R$ be a relation between $\alpha$ and $\beta$ that is
recursively enumerable as a predicate on pairs $(a, b)$. Then there is a partial recursive
function $g$ from $\alpha$ to $\beta$ such that, for every $a \in \alpha$, if $g(a)$ is defined
then its value $b$ satisfies $R(a, b)$, and $g(a)$ is defined whenever some $b \in \beta$
satisfies $R(a, b)$.

The proof searches over pairs of a candidate $b$ and a step bound by dovetailing with the
step-bounded simulation of the semi-decision procedure for $R$.

Formalized by `MetaMathlibExt.REPred.exists_partrec_choose`, a theorem declared in [MathlibExt/Computability/RE.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Computability/RE.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#exists-partrec-choose).

## Existential projection preserves recursive enumerability

Let $\alpha$ and $\beta$ be
types with primitive recursive encodings into $\mathbb{N}$, and let $R$ be a relation between
$\alpha$ and $\beta$ that is recursively enumerable as a predicate on pairs $(a, b)$. Then the
predicate $a \mapsto \exists b \in \beta,\ R(a, b)$ is recursively enumerable.

The predicate is the domain of the partial recursive function that selects a witness of $R$.

Formalized by `MetaMathlibExt.REPred.exists`, a theorem declared in [MathlibExt/Computability/RE.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Computability/RE.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#exists).

## Decidability by multi-stack machines

Let $\alpha$ be a primcodable type (it has an
encoding $\mathrm{encode} : \alpha \to \mathbb{N}$ whose decoding is primitive recursive). A
predicate $p$ on $\alpha$ is decidable by a multi-stack machine when there is a function
$f : \mathbb{N} \to \mathbb{N}$ computed by a multi-stack Turing machine, with input and output
numbers written in binary, such that for every $a \in \alpha$, $f(\mathrm{encode}(a)) = 1$ if and
only if $p(a)$.

Formalized by `Cslib.Decidability.TM2Decidable`, a definition declared in [CSLibExt/Computability/Decidability/Basic.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Basic.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#tm2-decidable).

## Recognizability by multi-stack machines

Let $\alpha$ be a primcodable type (it has an
encoding $\mathrm{encode} : \alpha \to \mathbb{N}$ whose decoding is primitive recursive). A
predicate $p$ on $\alpha$ is recognizable by a multi-stack machine when there are a multi-stack
Turing machine $M$ and an identification of its input alphabet with the Booleans such that for
every $a \in \alpha$, $p(a)$ holds if and only if $M$ halts when started on the binary word of
$\mathrm{encode}(a)$.

Formalized by `Cslib.Decidability.TM2Recognizable`, a definition declared in [CSLibExt/Computability/Decidability/Basic.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Basic.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#tm2-recognizable).

## Co-recognizability by multi-stack machines

Let $\alpha$ be a primcodable type (it has an
encoding $\mathrm{encode} : \alpha \to \mathbb{N}$ whose decoding is primitive recursive). A
predicate $p$ on $\alpha$ is co-recognizable by a multi-stack machine when its complement
$\neg p$ is recognizable by a multi-stack machine.

Formalized by `Cslib.Decidability.TM2CoRecognizable`, a definition declared in [CSLibExt/Computability/Decidability/Basic.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Basic.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#tm2-co-recognizable).

## Multi-stack decidable predicates are exactly the computable predicates

Let $\alpha$ be a
primcodable type (it has an encoding $\mathrm{encode} : \alpha \to \mathbb{N}$ whose decoding is
primitive recursive). A predicate $p$ on $\alpha$ is decidable by a multi-stack machine if and
only if it is computable, that is, $p$ is decidable and its Boolean characteristic function
$\alpha \to \mathrm{Bool}$ is computable.

Formalized by `Cslib.Decidability.tm2Decidable_iff_computablePred`, a theorem declared in [CSLibExt/Computability/Decidability/Basic.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Basic.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#tm2-decidable-iff-computable-pred).

## Multi-stack recognizable predicates are exactly the r.e. predicates

Let $\alpha$ be a
primcodable type (it has an encoding $\mathrm{encode} : \alpha \to \mathbb{N}$ whose decoding is
primitive recursive). A predicate $p$ on $\alpha$ is recognizable by a multi-stack machine if and
only if it is recursively enumerable, that is, the partial function on $\alpha$ that is defined,
with a trivial value, exactly where $p$ holds is partial recursive.

Formalized by `Cslib.Decidability.tm2Recognizable_iff_rePred`, a theorem declared in [CSLibExt/Computability/Decidability/Basic.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Basic.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#tm2-recognizable-iff-re-pred).

## Multi-stack co-recognizable predicates are exactly the co-r.e. predicates

Let $\alpha$ be
a primcodable type (it has an encoding $\mathrm{encode} : \alpha \to \mathbb{N}$ whose decoding is
primitive recursive). A predicate $p$ on $\alpha$ is co-recognizable by a multi-stack machine if
and only if its complement $\neg p$ is recursively enumerable, that is, the partial function on
$\alpha$ that is defined, with a trivial value, exactly where $\neg p$ holds is partial
recursive.

Formalized by `Cslib.Decidability.tm2CoRecognizable_iff_rePred_not`, a theorem declared in [CSLibExt/Computability/Decidability/Basic.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Basic.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#tm2-co-recognizable-iff-re-pred-not).

## Decidable predicates are recognizable by multi-stack machines

Let $\alpha$ be a
primcodable type (it has an encoding $\mathrm{encode} : \alpha \to \mathbb{N}$ whose decoding is
primitive recursive). If a predicate $p$ on $\alpha$ is decidable by a multi-stack machine, then
$p$ is recognizable by a multi-stack machine.

Formalized by `Cslib.Decidability.TM2Decidable.tm2Recognizable`, a theorem declared in [CSLibExt/Computability/Decidability/Basic.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Basic.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#tm2-recognizable-2).

## Decidability by multi-stack machines is closed under complement

Let $\alpha$ be a
primcodable type (it has an encoding $\mathrm{encode} : \alpha \to \mathbb{N}$ whose decoding is
primitive recursive). If a predicate $p$ on $\alpha$ is decidable by a multi-stack machine, then
so is its complement $\neg p$.

Formalized by `Cslib.Decidability.TM2Decidable.not`, a theorem declared in [CSLibExt/Computability/Decidability/Basic.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Basic.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#not).

## Decidable predicates are co-recognizable by multi-stack machines

Let $\alpha$ be a
primcodable type (it has an encoding $\mathrm{encode} : \alpha \to \mathbb{N}$ whose decoding is
primitive recursive). If a predicate $p$ on $\alpha$ is decidable by a multi-stack machine, then
$p$ is co-recognizable by a multi-stack machine, that is, its complement $\neg p$ is recognizable
by a multi-stack machine.

Formalized by `Cslib.Decidability.TM2Decidable.tm2CoRecognizable`, a theorem declared in [CSLibExt/Computability/Decidability/Basic.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Basic.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#tm2-co-recognizable-2).

## Post's theorem for multi-stack machines

Let $\alpha$ be a primcodable type (it has an
encoding $\mathrm{encode} : \alpha \to \mathbb{N}$ whose decoding is primitive recursive). A
predicate $p$ on $\alpha$ is decidable by a multi-stack machine if and only if it is both
recognizable and co-recognizable by a multi-stack machine.

Formalized by `Cslib.Decidability.tm2Decidable_iff_tm2Recognizable_and_tm2CoRecognizable`, a theorem declared in [CSLibExt/Computability/Decidability/Basic.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Basic.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#tm2-decidable-iff-tm2-recognizable-and-t).

## Decidable predicates are closed under conjunction

Let $p$ and $q$ be predicates on a
type $\alpha$ with a primitive recursive encoding. If $p$ and $q$ are both decidable by
multi-stack machines, then so is the predicate $a \mapsto p(a) \wedge q(a)$.

Formalized by `Cslib.Decidability.TM2Decidable.and`, a theorem declared in [CSLibExt/Computability/Decidability/Closure.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Closure.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#and-3).

## Decidable predicates are closed under disjunction

Let $\alpha$ be a type with a
primitive recursive encoding. If $p$ and $q$ are predicates on $\alpha$ that are decidable by a
multi-stack Turing machine, then so is the predicate $a \mapsto p(a) \lor q(a)$.

Formalized by `Cslib.Decidability.TM2Decidable.or`, a theorem declared in [CSLibExt/Computability/Decidability/Closure.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Closure.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#or-3).

## Recognizable predicates are closed under conjunction

Let $p$ and $q$ be predicates
on a type $\alpha$ with a primitive recursive encoding. If $p$ and $q$ are both recognizable
by multi-stack machines, then so is the predicate $a \mapsto p(a) \wedge q(a)$.

Formalized by `Cslib.Decidability.TM2Recognizable.and`, a theorem declared in [CSLibExt/Computability/Decidability/Closure.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Closure.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#and-4).

## Recognizable predicates are closed under disjunction

Let $\alpha$ be a type with a
primitive recursive encoding. If $p$ and $q$ are predicates on $\alpha$ that are recognizable by
a multi-stack Turing machine, then so is the predicate $a \mapsto p(a) \lor q(a)$.

Formalized by `Cslib.Decidability.TM2Recognizable.or`, a theorem declared in [CSLibExt/Computability/Decidability/Closure.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Closure.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#or-4).

## Language of a Boolean test

For a Boolean-valued function $f$ on words over an
alphabet $\sigma$, the language of $f$ is the set of words $u$ over $\sigma$ with
$f(u) = \mathrm{true}$.

Formalized by `Cslib.Decidability.boolLang`, a definition declared in [CSLibExt/Computability/Decidability/Closure.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Closure.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#bool-lang).

## Membership in a concatenation of languages

For languages $L_1$ and $L_2$ over an
alphabet $\sigma$ and a word $w$ over $\sigma$, $w$ lies in the concatenation $L_1 L_2$ if and
only if there are words $u$ and $v$ with $w = uv$, $u \in L_1$ and $v \in L_2$.

Formalized by `Cslib.Decidability.mem_mul_iff_exists_append`, a theorem declared in [CSLibExt/Computability/Decidability/Closure.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Closure.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#mem-mul-iff-exists-append).

## Bounded split test

Given Boolean tests $f$ and $g$ on words over $\sigma$, a word $w$ and
a natural number $n$, the split test is the Boolean value that is true exactly when there is some
$i < n$ such that $f$ is true on the prefix of $w$ of length $\min(i, |w|)$ and $g$ is true on
the remaining suffix of $w$.

Formalized by `Cslib.Decidability.splitTest`, a definition declared in [CSLibExt/Computability/Decidability/Closure.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Closure.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#split-test).

## Decidable languages have computable membership tests

Let $L$ be a language over an
alphabet $\sigma$ with a primitive recursive encoding. If membership in $L$ is decidable by a
multi-stack machine, then there is a computable function $f$ from words over $\sigma$ to
Booleans such that $L$ is the language of $f$, that is, the set of words $u$ with
$f(u) = \mathrm{true}$.

Formalized by `Cslib.Decidability.TM2Decidable.exists_computable`, a theorem declared in [CSLibExt/Computability/Decidability/Closure.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Closure.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#exists-computable).

## Decidable languages are closed under concatenation

Let $\sigma$ be an alphabet with a
primitive recursive encoding. If $L_1$ and $L_2$ are languages over $\sigma$ whose membership
predicates are decidable by a multi-stack Turing machine, then the membership predicate of their
concatenation $L_1 L_2 = \{uv : u \in L_1, v \in L_2\}$ is also decidable by a multi-stack
Turing machine.

Formalized by `Cslib.Decidability.TM2Decidable.mul`, a theorem declared in [CSLibExt/Computability/Decidability/Closure.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Closure.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#mul).

## Splits of a word

For a word $w$ over $\sigma$ of length $n$, this is the list of the
$n + 1$ pairs $(u, v)$ of words with $uv = w$, ordered by the length of $u$: for each
$i = 0, 1, \dots, n$ it contains the prefix of $w$ of length $i$ paired with the remaining
suffix.

Formalized by `Cslib.Decidability.splits`, a definition declared in [CSLibExt/Computability/Decidability/Closure.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Closure.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#splits).

## Recognizable languages are closed under concatenation

Let $L_1$ and $L_2$ be
languages over an alphabet $\sigma$ with a primitive recursive encoding. If membership in $L_1$
and membership in $L_2$ are recognizable by multi-stack machines, then so is membership in the
concatenation $L_1 L_2$, the set of words $uv$ with $u \in L_1$ and $v \in L_2$.

Formalized by `Cslib.Decidability.TM2Recognizable.mul`, a theorem declared in [CSLibExt/Computability/Decidability/Closure.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Closure.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#mul-2).

## Extending a list of pieces by a letter

Given a letter $a$ and a list
$\pi = [u_1, \dots, u_k]$ of words, the extensions of $\pi$ by $a$ are listed as follows: first
$[[a], u_1, \dots, u_k]$, which starts a new piece $[a]$, and then, only when $k \ge 1$, also
$[a u_1, u_2, \dots, u_k]$, which puts the letter $a$ in front of the first piece.

Formalized by `Cslib.Decidability.extendPartitions`, a definition declared in [CSLibExt/Computability/Decidability/Closure.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Closure.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#extend-partitions).

## Partitions of a word into nonempty factors

For a word $w$ over $\sigma$, this is the
list of all ways to write $w$ as a concatenation $w = u_1 u_2 \cdots u_k$ of nonempty words
$u_1, \dots, u_k$, each recorded as the list $[u_1, \dots, u_k]$. The empty word has exactly one
such partition, the empty list.

Formalized by `Cslib.Decidability.partitions`, a definition declared in [CSLibExt/Computability/Decidability/Closure.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Closure.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#partitions).

## Recognizable languages are closed under Kleene star

Let $L$ be a language over an
alphabet $\sigma$ with a primitive recursive encoding. If membership in $L$ is recognizable by
a multi-stack machine, then so is membership in the Kleene star $L^*$, the set of all
concatenations $u_1 \cdots u_k$ with $k \ge 0$ and $u_1, \dots, u_k \in L$.

Formalized by `Cslib.Decidability.TM2Recognizable.kstar`, a theorem declared in [CSLibExt/Computability/Decidability/Closure.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Closure.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#kstar).

## Decidable languages are closed under Kleene star

Let $L$ be a language over an
alphabet $\sigma$ with a primitive recursive encoding. If membership in $L$ is decidable by a
multi-stack machine, then so is membership in the Kleene star $L^*$, the set of all
concatenations $u_1 \cdots u_k$ with $k \ge 0$ and $u_1, \dots, u_k \in L$.

Formalized by `Cslib.Decidability.TM2Decidable.kstar`, a theorem declared in [CSLibExt/Computability/Decidability/Closure.lean, line 316](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Closure.lean#L316). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#kstar-2).

## Recognizable languages are closed under alphabet maps

Let $\sigma$ and $\tau$ be
alphabets with primitive recursive encodings, let $f : \sigma \to \tau$ be primitive recursive,
and let $L$ be a language over $\sigma$. If membership in $L$ is recognizable by a multi-stack
machine, then so is membership in the image language
$f(L) = \{f(a_1) \cdots f(a_n) : a_1 \cdots a_n \in L\}$, obtained by applying $f$ letter by
letter to the words of $L$.

The recognizer searches for a preimage word by unbounded dovetailing. Every map between finite
alphabets is primitive recursive.

Formalized by `Cslib.Decidability.TM2Recognizable.map`, a theorem declared in [CSLibExt/Computability/Decidability/Closure.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Closure.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html#map).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Decidable and recognizable predicates](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/computability/decidable-and-recognizable-predicates)
