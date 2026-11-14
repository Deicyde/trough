# Pigeon-hole and double counting

Some mathematical principles, such as the two in the title of this chapter, are so obvious that you might think they would only produce equally obvious results. To convince you that “It ain't necessarily so” we illustrate them with examples that were suggested by Paul Erdős to be included in The Book. We will encounter instances of them also in later chapters.

- [Pigeon-hole principle](pigeon-hole-principle.md)

Well, this is indeed obvious, there is nothing to prove. In the language of mappings our principle reads as follows: Let $N$ and $R$ be two finite sets with $|N| = n > r = |R|$, and let $f : N \to R$ be a mapping. Then there exists some $a \in R$ with $|f^{-1}(a)| \geq 2$. We may even state a stronger inequality: There exists some $a \in R$ with

$$
|f^{-1}(a)| \geq \left\lceil \frac{n}{r} \right\rceil.
$$

In fact, otherwise we would have $|f^{-1}(a)| < \frac{n}{r}$ for all $a$, and hence $n = \sum_{a \in R} |f^{-1}(a)| < r \cdot \frac{n}{r} = n$, which cannot be.

*The proof of [Pigeon-hole principle](pigeon-hole-principle.md) is shown with its statement.*

- [Numbers](numbers/README.md)
- [Sequences](sequences/README.md)
- [Sums](sums/README.md)
- [Numbers again](numbers-again/README.md)
- [Graphs](graphs/README.md)
- [Sperner's Lemma](sperners-lemma/README.md)
