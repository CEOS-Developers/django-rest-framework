package dev.ceos.springrestframework.model;

import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.annotation.LastModifiedDate;

import java.util.Date;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Lob;

@Entity
public class Post {

    private Post() {}

    public Post(String text, Integer likeCount) {
        this.text = text;
        this.likesCount = likeCount;
    }

    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Id
    private Long id;

    @Column
    @Lob
    private String text;

    @Column
    private Integer likesCount;

    @CreatedDate
    @Column
    private Date createdAt;

    @LastModifiedDate
    @Column
    private Date updatedAt;

    public Long getId() {
        return id;
    }

    public String getText() {
        return text;
    }

    public Integer getLikesCount() {
        return likesCount;
    }

    public Date getCreatedAt() {
        return createdAt;
    }

    public Date getUpdatedAt() {
        return updatedAt;
    }

    @Override
    public String toString() {
        return "Post{" +
                "id=" + id +
                ", text='" + text + '\'' +
                ", likesCount=" + likesCount +
                ", createdAt=" + createdAt +
                ", updatedAt=" + updatedAt +
                '}';
    }
}