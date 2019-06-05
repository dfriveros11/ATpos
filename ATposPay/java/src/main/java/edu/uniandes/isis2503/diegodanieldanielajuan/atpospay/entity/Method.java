package edu.uniandes.isis2503.diegodanieldanielajuan.atpospay.entity;

import java.io.Serializable;

import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.ManyToOne;
import com.fasterxml.jackson.annotation.JsonBackReference;

@Entity
public class Method implements Serializable {
	
	/**
	 * Serializable
	 */
	private static final long serialVersionUID = 6287805956991986743L;

	/**
	 * Id of the Product
	 */
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private long id;
	
	private String name;
	
	private String description;

	
	@JsonBackReference(value="PayMethod")
	@ManyToOne(fetch=FetchType.EAGER)
	private Pay pay;
	
	
	public Method(){}


	public Method(String name, String description, Pay pay) {
		super();
		this.name = name;
		this.description = description;
		this.pay = pay;
	}


	public long getId() {
		return id;
	}


	public void setId(long id) {
		this.id = id;
	}


	public String getName() {
		return name;
	}


	public void setName(String name) {
		this.name = name;
	}


	public String getDescription() {
		return description;
	}


	public void setDescription(String description) {
		this.description = description;
	}


	public Pay getPay() {
		return pay;
	}


	public void setPay(Pay bill) {
		this.pay = bill;
	}
	


}
