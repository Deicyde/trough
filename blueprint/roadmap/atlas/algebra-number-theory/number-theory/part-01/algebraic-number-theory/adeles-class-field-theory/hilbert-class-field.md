---
declaration: section
origin: cited
lean: NumberField.IsHilbertClassField, NumberField.IsHilbertClassField.apply_maximal
statement: formalized
proof: formalized
---

# Hilbert class field

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/hilbert-class-field/index.html).

## Hilbert class field of a number field

Let $K$ and $L$ be number fields with $L$ an
extension of $K$. Then $L$ is a Hilbert class field of $K$ if $L/K$ is a finite-dimensional
abelian Galois extension, every nonzero prime ideal of the ring of integers $\mathcal{O}_K$ is
unramified in $\mathcal{O}_L$, every infinite place of $L$ is unramified over $K$, and $L$ is
maximal with these properties: every number field $M$ that is a finite-dimensional abelian Galois
extension of $K$, such that every nonzero prime ideal of $\mathcal{O}_K$ is unramified in
$\mathcal{O}_M$ and every infinite place of $M$ is unramified over $K$, admits a $K$-algebra
homomorphism $M \to L$.

Formalized by `NumberField.IsHilbertClassField`, a structure declared in [MathlibExt/NumberTheory/NumberField/HilbertClassField.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/HilbertClassField.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/hilbert-class-field/index.html#is-hilbert-class-field).

## Abelian unramified extensions embed in the Hilbert class field

Let $K$ and $L$ be number
fields with $L$ an extension of $K$ that is a Hilbert class field of $K$. If $M$ is a number field
that is a finite-dimensional abelian Galois extension of $K$, such that every nonzero prime ideal
of the ring of integers $\mathcal{O}_K$ is unramified in $\mathcal{O}_M$ and every infinite place
of $M$ is unramified over $K$, then there is a $K$-algebra homomorphism $M \to L$.

Formalized by `NumberField.IsHilbertClassField.apply_maximal`, a theorem declared in [MathlibExt/NumberTheory/NumberField/HilbertClassField.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/HilbertClassField.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/hilbert-class-field/index.html#apply-maximal).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hilbert class field](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/hilbert-class-field/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/hilbert-class-field)
